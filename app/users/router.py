from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from app.core.logger import logger
from app.users.schemas import User, UserInDB, UserDuringRegistration, Token
from app.users.services import (
    authenticate_user,
    create_access_token,
    get_current_active_user,
    add_user
)


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/register", status_code=201)
async def register_user(
        user_data: UserDuringRegistration = Depends()
) -> None:
    return await add_user(user_data)


@router.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> dict[str, str]:
    user = await authenticate_user(form_data.username, form_data.password)
    access_token = await create_access_token(data={"sub": user.name})

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=User)
async def read_users_me(
        current_user: Annotated[UserInDB, Depends(get_current_active_user)]
) -> UserInDB:
    return current_user


logger.info(msg='init users routers')
