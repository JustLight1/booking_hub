from sqlalchemy import JSON, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


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
    hotel = relationship('Hotels', back_populates='rooms')
    booking = relationship('Bookings', back_populates='room')

    def __str__(self) -> str:
        return f'Номер {self.name}'
