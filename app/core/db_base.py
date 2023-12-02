from sqlalchemy import delete, insert, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app.core import settings
from app.core.logger import logger


class Base(DeclarativeBase):
    pass


dsn = settings.TEST_DSN if settings.MODE == 'TEST' else settings.DSN

async_engine = create_async_engine(
    url=dsn,
    # echo=True,
)

async_session_maker = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
)


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        try:
            async with async_session_maker() as session:
                query = select(cls.model.__table__.columns) \
                    .filter_by(**filter_by)
                result = await session.execute(query)
                return result.mappings().one_or_none()

        except (SQLAlchemyError, Exception) as e:
            await cls.error_logging(
                e=e,
                msg="Cannot find data in table",
            )

    @classmethod
    async def find_all(cls, **filter_by):
        try:
            async with async_session_maker() as session:
                query = select(cls.model.__table__.columns) \
                    .filter_by(**filter_by)
                result = await session.execute(query)
                return result.mappings().all()

        except (SQLAlchemyError, Exception) as e:
            await cls.error_logging(
                e=e,
                msg="Cannot find data in table",
            )

    @classmethod
    async def add(cls, **data):
        try:
            async with async_session_maker() as session:
                query = insert(cls.model).values(**data) \
                    .returning(cls.model.id)
                result = await session.execute(query)
                await session.commit()
                return result.mappings().first()

        except (SQLAlchemyError, Exception) as e:
            await cls.error_logging(
                e=e,
                msg="Cannot insert data into table",
            )

    @classmethod
    async def delete(cls, **filter_by) -> None:
        try:
            async with async_session_maker() as session:
                query = delete(cls.model).filter_by(**filter_by)
                await session.execute(query)
                await session.commit()

        except (SQLAlchemyError, Exception) as e:
            await cls.error_logging(
                e=e,
                msg="Cannot delete data from table",
            )

    @classmethod
    async def error_logging(cls, e: Exception, msg: str) -> None:
        if isinstance(e, SQLAlchemyError):
            msg = "Database Exc: " + msg

        elif isinstance(e, Exception):
            msg = "Unknown Exc: " + msg

        logger.error(
            msg=msg,
            extra={
                "table": cls.model.__tablename__,
            },
            exc_info=True
        )


logger.info(msg='init db base')
