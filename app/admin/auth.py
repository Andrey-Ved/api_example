from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse

from app.core.exceptions import UnauthorizedException
from app.core.logger import logger
from app.users.services import create_access_token, authenticate_user, get_current_user


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request):
        form = await request.form()

        try:
            user = await authenticate_user(
                username=form["username"],
                password=form["password"]
            )
            access_token = await create_access_token(
                data={"sub": user.name}
            )

        except UnauthorizedException:
            return RedirectResponse(
                url=request.url_for("admin:login"),
                status_code=302,
            )

        request.session.update({"access_token": access_token})
        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request):
        access_token = request.session.get("access_token")

        if not access_token:
            return False

        try:
            await get_current_user(access_token)
        except UnauthorizedException:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        return True


authentication_backend = AdminAuth(secret_key="...")

logger.info(msg='init sqladmin auth')
