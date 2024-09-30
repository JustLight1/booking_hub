from datetime import datetime

from app.bookings.dao import BookingDAO
from app.database import async_session_maker


async def test_add_and_get_booking():
    async with async_session_maker() as session:
        new_booking = await BookingDAO.add(
            user_id=2,
            room_id=2,
            date_from=datetime.strptime('2023-07-10', '%Y-%m-%d'),
            date_to=datetime.strptime('2023-07-20', '%Y-%m-%d'),
            session=session
        )
        assert new_booking.user_id == 2
        assert new_booking.room_id == 2

        new_booking = await BookingDAO.find_by_id(
            session,
            model_id=new_booking.id
        )

        assert new_booking is not None
