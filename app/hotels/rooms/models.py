from typing import TYPE_CHECKING

from sqlalchemy import JSON, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base

if TYPE_CHECKING:
    from app.hotels.models import Hotels
    from app.bookings.models import Bookings


class Rooms(Base):
    hotel_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('hotels.id'), nullable=False
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    services: Mapped[dict] = mapped_column(JSON, nullable=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    image_id: Mapped[int] = mapped_column(Integer)

    hotel: Mapped['Hotels'] = relationship('Hotels', back_populates='rooms')
    booking: Mapped[list['Bookings']] = relationship(
        'Bookings', back_populates='room')

    def __str__(self):
        return f'Номер {self.name}'
