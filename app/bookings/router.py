from datetime import date
from fastapi import APIRouter, Depends

from users.dependencies import get_current_user
from users.models import Users
from .dao import BookingDAO
from .schemas import SBooking
from exceptions import RoomCannotBeBooked

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get('')
async def get_bookings(
    user: Users = Depends(get_current_user)
) -> list[SBooking]:
    result = await BookingDAO.find_all(user_id=user.id)
    return result


@router.post('')
async def add_booking(
    room_id: int, date_from: date, date_to: date,
    user: Users = Depends(get_current_user)
):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked
