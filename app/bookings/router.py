from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking, SBookingInfo
from app.exceptions import (RoomCannotBeBooked, CannotDeleteBooking,
                            BookingDoesNotExistException)

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get("")
async def get_bookings(
    session: AsyncSession = Depends(get_async_session),
    user: Users = Depends(get_current_user)
) -> list[SBookingInfo]:
    return await BookingDAO.find_all_with_images(user.id, session)


@router.post('')
async def add_booking(
    room_id: int, date_from: date, date_to: date,
    session: AsyncSession = Depends(get_async_session),
    user: Users = Depends(get_current_user)
):
    booking = await BookingDAO.add(
        user.id, room_id, date_from, date_to, session
    )
    if not booking:
        raise RoomCannotBeBooked


@router.delete(
    '/',
    response_model=SBooking
)
async def remove_booking(
    booking_id: int,
    current_user: Users = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):
    bookings = await BookingDAO.find_one_or_none(session, id=booking_id)
    if not bookings:
        raise BookingDoesNotExistException
    if bookings.user_id != current_user.id:
        raise CannotDeleteBooking
    await BookingDAO.delete(
        session, id=booking_id, user_id=current_user.id
    )
    return bookings
