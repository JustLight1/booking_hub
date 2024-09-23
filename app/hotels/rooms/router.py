from datetime import date, datetime, timedelta

from fastapi import Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.hotels.rooms.dao import RoomDAO
from app.hotels.rooms.schemas import SRoomInfo
from app.hotels.router import router


@router.get(
    '/{hotel_id}/rooms',
    response_model=list[SRoomInfo]
)
# Этот эндпоинт можно и нужно кэшировать, но в курсе этого не сделано, чтобы
# можно было проследить разницу в работе /rooms (без кэша) и /hotels (с кэшем).
async def get_rooms_by_time(
    hotel_id: int,
    date_from: date = Query(
        ..., description=f'Например, {datetime.now().date()}'
    ),
    date_to: date = Query(
        ..., description=(
            f'Например, {(datetime.now() + timedelta(days=14)).date()}'
        )
    ),
    session: AsyncSession = Depends(get_async_session)
):
    rooms = await RoomDAO.find_all(hotel_id, date_from, date_to, session)
    return rooms
