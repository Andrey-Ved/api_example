from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import DeclarativeBase
from typing import Type

from app.core import settings
from app.core.logger import logger


db_file = settings.TEST_DATABASE_FILE \
    if settings.MODE == 'TEST' \
    else settings.DATABASE_FILE


async def db_init(
        async_engine:  AsyncEngine,
        base: Type[DeclarativeBase]
) -> None:

    async with async_engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)

        for table in base.metadata.sorted_tables:
            logger.info(
                msg='init table',
                extra={
                    "db": db_file,
                    "table": table,
                },
            )

    logger.info(msg='init base metadata')


async def db_clear(
        async_engine:  AsyncEngine,
        base: Type[DeclarativeBase]
) -> None:

    async with async_engine.begin() as conn:
        await conn.run_sync(base.metadata.reflect)

        for table in base.metadata.sorted_tables:
            await conn.execute(table.delete())

            logger.info(
                msg='clear table in db',
                extra={
                    "db": db_file,
                    "table": table,
                },
            )


logger.info(msg='init db services')
