import sentry_sdk

from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core import settings
from app.core.db_base import Base, async_engine
from app.core.db_services import db_init, db_clear
from app.core.logger import logger


async def start_app():
    logger.info(msg='start app', )

    await db_init(async_engine, Base)

    if settings.MODE == 'TEST':
        await db_clear(async_engine, Base)

    else:
        if settings.SENTRY_DSN:
            sentry_sdk.init(
                dsn=settings.SENTRY_DSN,
                traces_sample_rate=1.0,
                profiles_sample_rate=1.0,
            )


async def stop_app():
    if settings.DB_CLEAR_AT_THE_END:
        await db_clear(async_engine, Base)

    logger.info(msg='stop app', )


@asynccontextmanager
async def lifespan(application: FastAPI):  # noqa
    await start_app()
    yield
    await stop_app()
