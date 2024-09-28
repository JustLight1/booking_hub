from fastapi import Request, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from jose import jwt, JWTError, ExpiredSignatureError

from app.config import settings
from app.database import get_async_session
from app.users.dao import UsersDAO
from app.exceptions import (IncorrectTokenFormatException,
                            TokenExpiredException, UserIsNotPresentException,
                            TokenAbsentException)


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(
        token: str = Depends(get_token),
        session: AsyncSession = Depends(get_async_session)
):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except ExpiredSignatureError:
        raise TokenExpiredException
    except JWTError:
        raise IncorrectTokenFormatException
    user_id: str = payload.get('sub')
    if not user_id:
        raise UserIsNotPresentException
    user = await UsersDAO.find_one_or_none(session, id=int(user_id))
    if not user:
        raise UserIsNotPresentException
    return user
