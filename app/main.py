from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel
import uvicorn

from bookings.router import router as router_bookings
from users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)


class Hotel:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


@app.get('/hotels/')
def get_hotels(
    search_args: Hotel = Depends()
):

    return search_args


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info',
                reload=True)
