from datetime import date

from sqlalchemy import func, insert, select, and_, or_
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.bookings.models import Bookings
from app.hotels.rooms.models import Rooms
from app.exceptions import RoomCannotBeBooked


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def find_all_by_user(cls, user_id: int, session: AsyncSession):
        query = (
            select(
                # __table__.columns нужен для отсутствия вложенности в ответе Алхимии
                Bookings.__table__.columns,
                Rooms.__table__.columns,
                Bookings.total_days.label("total_days"),
                Bookings.total_cost.label("total_cost")
            )
            .join(Rooms, Rooms.id == Bookings.room_id, isouter=True)
            .where(Bookings.user_id == user_id)
        )
        result = await session.execute(query)
        return result.mappings().all()

    @classmethod
    async def add(
        cls,
        user_id: int,
        room_id: int,
        date_from: date,
        date_to: date,
        session: AsyncSession
    ):
        """
        WITH booked_rooms AS (
            SELECT * FROM bookings
            WHERE room_id = 1 AND
            (date_from >= '2023-05-15' AND date_from <= '2023-06-20') OR
            (date_from <= '2023-05-15' AND date_to > '2023-05-15')
        )
        SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
        LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
        WHERE rooms.id = 1
        GROUP BY rooms.quantity, booked_rooms.room_id
        """
        booked_rooms = select(Bookings).where(
            and_(
                Bookings.room_id == room_id,
                or_(
                    and_(
                        Bookings.date_from >= date_from,
                        Bookings.date_from <= date_to
                    ),
                    and_(
                        Bookings.date_from <= date_from,
                        Bookings.date_to > date_from
                    ),
                )
            )
        ).cte('booked_rooms')

        get_rooms_left = select(
            Rooms.quantity - func.count(booked_rooms.c.room_id)
        ).select_from(Rooms).join(
            booked_rooms, booked_rooms.c.room_id == Rooms.id,
            isouter=True
        ).where(Rooms.id == room_id).group_by(
            Rooms.quantity, booked_rooms.c.room_id
        )

        # print(get_rooms_left.compile(
        #     engine, compile_kwargs={'literal_bind': True}
        #     ))

        rooms_left = await session.execute(get_rooms_left)
        rooms_left: int = rooms_left.scalar()

        if rooms_left > 0:
            get_price = select(Rooms.price).filter_by(id=room_id)
            price = await session.execute(get_price)
            price: int = price.scalar()
            add_booking = insert(Bookings).values(
                room_id=room_id,
                user_id=user_id,
                date_from=date_from,
                date_to=date_to,
                price=price,
            ).returning(
                Bookings.id,
                Bookings.user_id,
                Bookings.room_id,
                Bookings.date_from,
                Bookings.date_to,
            )

            new_booking = await session.execute(add_booking)
            await session.commit()
            return new_booking.scalar()
        else:
            raise RoomCannotBeBooked
