from datetime import datetime

from app.hotels.dao import HotelsDAO
from app.database import async_session_maker


async def test_get_hotels_by_location_and_time():
    async with async_session_maker() as session:
        get_hotels = await HotelsDAO.find_all(
            location='Алтай',
            date_from=datetime.strptime('2023-07-10', '%Y-%m-%d'),
            date_to=datetime.strptime('2023-07-20', '%Y-%m-%d'),
            session=session
        )

        assert get_hotels is not None
