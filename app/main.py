import uvicorn

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi_versioning import VersionedFastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from sqladmin import Admin
from time import time

from app.admin.auth import authentication_backend
from app.admin.views import NotesAdmin, UsersAdmin
from app.core import settings
from app.core.db_base import async_engine
from app.core.lifespan import lifespan
from app.core.logger import logger
from app.notes.router import router as router_notes
from app.users.router import router as router_auth


app = FastAPI(lifespan=lifespan)

app.include_router(router_auth)
app.include_router(router_notes)

origins = [
    f"http://localhost:{settings.API_PORT}",
    f"http://127.0.0.1:{settings.API_PORT}",
    # f"http://127.0.0.1",
    # f"http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[
        "GET",
        "POST",
        "OPTIONS",
        "DELETE",
        "PATCH",
        "PUT",
    ],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)

app = VersionedFastAPI(app,
                       version_format='{major}',
                       prefix_format='/v{major}',
                       description='Greet users with a nice message',
                       lifespan=lifespan,
                       )


@app.get("/")
async def root() -> Response:
    return RedirectResponse(url="/v2/docs", status_code=301)


if settings.TIME_HEADER_LOGGING:
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start_time = time()
        response = await call_next(request)
        process_time = time() - start_time

        logger.info(
            msg="Request handling time",
            extra={
                "process_time": round(process_time, 4),
            },
        )
        return response


instrumentator = Instrumentator(                  # noqa
    should_group_status_codes=False,
    excluded_handlers=[".*admin.*", "/metrics"],
)
instrumentator.instrument(app).expose(app)

admin = Admin(
    app=app,
    engine=async_engine,
    authentication_backend=authentication_backend
)

admin.add_view(UsersAdmin)
admin.add_view(NotesAdmin)


def main():
    print(
        f'\n'
        f'INFO:     Documentation is available at -'
        f' http://127.0.0.1:{settings.API_PORT}/v2/docs'
        f'\n'
        f'INFO:     SQLAdmin interface is available at -'
        f' http://127.0.0.1:{settings.API_PORT}/admin'
        f'\n'
    )

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=settings.API_PORT
    )


if __name__ == '__main__':
    main()
