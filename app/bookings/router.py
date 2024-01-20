from fastapi import APIRouter, Depends

from users.dependencies import get_current_user
from users.models import Users
from .dao import BookingDAO

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)):
    result = await BookingDAO.find_all(user_id=user.id)
    return result
