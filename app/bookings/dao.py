from dao.base import BaseDAO
from bookings.models import Bookings


class BookingDAO(BaseDAO):
    model = Bookings
