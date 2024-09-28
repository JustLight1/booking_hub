from sqlalchemy import JSON, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Hotels(Base):
    name: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    services: Mapped[dict] = mapped_column(JSON)
    rooms_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    image_id: Mapped[int] = mapped_column(Integer)
    rooms = relationship('Rooms', back_populates='hotel')

    def __str__(self) -> str:
        return f'Отель {self.name} {self.location[:30]}'
