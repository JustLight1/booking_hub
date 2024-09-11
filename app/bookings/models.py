from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, Computed
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Bookings(Base):
    room_id: Mapped[int] = mapped_column(Integer, ForeignKey('rooms.id'))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    date_from: Mapped[date] = mapped_column(Date, nullable=False)
    date_to: Mapped[date] = mapped_column(Date, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)

    total_cost = mapped_column(
        Integer, Computed('date_to - date_from) * price'))
    total_days = mapped_column(Integer, Computed('date_to - date_from'))
