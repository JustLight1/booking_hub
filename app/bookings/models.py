from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, Computed
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Bookings(Base):
    room_id: Mapped[int] = mapped_column(Integer, ForeignKey('rooms.id'))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    date_from: Mapped[date] = mapped_column(Date, nullable=False)
    date_to: Mapped[date] = mapped_column(Date, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    total_cost: Mapped[int] = mapped_column(
        Integer, Computed('(date_to - date_from) * price'),
        nullable=True
    )
    total_days: Mapped[int] = mapped_column(
        Integer, Computed('date_to - date_from'),
        nullable=True
    )
    user = relationship('Users', back_populates='booking')
    room = relationship('Rooms', back_populates='booking')

    def __str__(self) -> str:
        return f'Booking #{self.id}'
