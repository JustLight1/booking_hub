from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import column_property
from database import Base


class Bookings(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    room_id = Column(ForeignKey('rooms.id'))
    user_id = Column(ForeignKey('users.id'))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)

    total_cost = column_property((date_to - date_from) * price)
    total_days = column_property((date_to - date_from))
