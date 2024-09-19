from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking, SBookingInfo, SNewBooking
from app.users.models import Users
from app.users.dependencies import get_current_user
from app.exceptions import (RoomCannotBeBooked, CannotDeleteBooking,
                            BookingDoesNotExistException)


router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get(
    '/',
    response_model=list[SBookingInfo]
)
async def get_booking(
    session: AsyncSession = Depends(get_async_session),
    user: Users = Depends(get_current_user)
):
    return await BookingDAO.find_all_by_user(user.id, session)


@router.post(
    '/',
    response_model=SNewBooking
)
async def add_bookings(
    room_id: int, date_from: date, date_to: date,
    user: Users = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session)
):
    booking = await BookingDAO.add(
        user.id, room_id, date_from, date_to, session
    )
    if not booking:
        raise RoomCannotBeBooked
    return booking


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
