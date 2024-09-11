from typing import TYPE_CHECKING

from sqlalchemy import JSON, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base


if TYPE_CHECKING:
    from app.hotels.rooms.models import Rooms


class Hotels(Base):
    name: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    services: Mapped[dict] = mapped_column(JSON)
    rooms_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    image_id: Mapped[int] = mapped_column(Integer)

    rooms_left: Mapped[int] = mapped_column(Integer, nullable=True)
    rooms: Mapped[list['Rooms']] = relationship(
        'Rooms', back_populates='hotel')

    def __str__(self):
        return f'Отель {self.name} {self.location[:30]}'
