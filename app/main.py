from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel
import uvicorn

from bookings.router import router as router_bookings
from users.router import router as router_users
from hotels.router import router as router_hotels
from hotels.rooms.router import router as router_rooms

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info',
                reload=True)
