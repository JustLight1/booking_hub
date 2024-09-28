from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Users(Base):
    email: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    booking = relationship('Bookings', back_populates='user')

    def __str__(self) -> str:
        return f'User {self.email}'
