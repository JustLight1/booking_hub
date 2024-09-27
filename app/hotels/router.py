from datetime import date, datetime, timedelta

from fastapi import APIRouter, Query, Depends
from fastapi_cache.decorator import cache

from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.exceptions import (CannotBookHotelForLongPeriod,
                            DateFromCannotBeAfterDateTo)
from app.hotels.dao import HotelsDAO
from app.hotels.schemas import SHotel, SHotelInfo


router = APIRouter(prefix='/hotels', tags=['Отели'])


@router.get(
    '/{location}',
    response_model=list[SHotelInfo]
)
@cache(expire=60)
async def get_hotels_by_location_and_time(
    location: str,
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
    if date_from > date_to:
        raise DateFromCannotBeAfterDateTo
    if (date_to - date_from).days > 31:
        raise CannotBookHotelForLongPeriod
    hotels = await HotelsDAO.find_all(location, date_from, date_to, session)
    return hotels


@router.get(
    '/id/{hotel_id}',
    response_model=SHotel | None
)
# Этот эндпоинт используется для фронтенда, когда мы хотим отобразить все
# номера в отеле и информацию о самом отеле. Этот эндпоинт как раз отвечает за
# информацию об отеле.
# В нем нарушается правило именования эндпоинтов: конечно же, /id/ здесь
# избыточен.Тем не менее, он используется, так как эндпоинтом ранее мы уже
# задали получение отелей по их локации вместо id.
async def get_hotel_by_id(
    hotel_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    return await HotelsDAO.find_one_or_none(session, id=hotel_id)
