from typing import Generic, Type, TypeVar

from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import Base


ModelType = TypeVar('ModelType', bound=Base)


class BaseDAO:
    model: Type[ModelType] = None

    @classmethod
    async def find_by_id(cls, session: AsyncSession, model_id: int):
        query = select(cls.model).filter_by(id=model_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, session: AsyncSession, **filter_by):
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, session: AsyncSession, **filter_by):
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def add(cls, session: AsyncSession, **data):
        query = insert(cls.model).values(**data)
        await session.execute(query)
        await session.commit()

    @classmethod
    async def delete(cls, session: AsyncSession, **filter_by):
        query = delete(cls.model).filter_by(**filter_by)
        await session.execute(query)
        await session.commit()
