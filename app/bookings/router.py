from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking, SBookingInfo
from app.exceptions import RoomCannotBeBooked

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get("")
async def get_bookings(
    session: AsyncSession = Depends(get_async_session),
    user: Users = Depends(get_current_user)
) -> list[SBookingInfo]:
    return await BookingDAO.find_all_with_images(user_id=user.id, session=session)


@router.post('')
async def add_booking(
    room_id: int, date_from: date, date_to: date,
    session: AsyncSession = Depends(get_async_session),
    user: Users = Depends(get_current_user)
):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to, session)
    if not booking:
        raise RoomCannotBeBooked


@router.delete("/{booking_id}")
async def remove_booking(
    booking_id: int,
    session: AsyncSession = Depends(get_async_session),
    current_user: Users = Depends(get_current_user),
):
    await BookingDAO.delete(id=booking_id, session=session, user_id=current_user.id)
