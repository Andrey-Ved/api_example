from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Annotated

from app.core import settings
from app.core.exceptions import (
    CannotAddDataToDatabase,
    IncorrectNameOrPasswordException,
    IncorrectTokenFormatException,
    UserIsNotPresentException,
    UserIsInactiveException,
    UserAlreadyExistsException,
)
from app.core.logger import logger
from app.users.dao import UserDAO
from app.users.schemas import (
    UserInDB,
    UserDuringRegistration,
    TokenData,
)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


async def create_access_token(
        data: dict,
        expires_delta: timedelta | None = None,
) -> str:
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def verify_password(
        plain_password: str,
        hashed_password: str) -> bool:
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def get_password_hash(
        password: str
) -> str:
    return pwd_context.hash(password)


async def get_user(
        username: str
) -> UserInDB:
    return await UserDAO.find_one_or_none(name=username)


async def authenticate_user(
        username: str,
        password: str
) -> UserInDB:
    user = await get_user(username)

    if not user:
        raise UserIsNotPresentException
    if not verify_password(password, user.hashed_password):
        raise IncorrectNameOrPasswordException

    return user


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)]
) -> UserInDB:
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")

        if username is None:
            raise UserIsNotPresentException

        token_data = TokenData(username=username)
    except JWTError:
        raise IncorrectTokenFormatException

    user = await get_user(username=token_data.username)

    if user is None:
        raise UserIsNotPresentException

    return user


async def get_current_active_user(
        current_user: Annotated[UserInDB, Depends(get_current_user)]
) -> UserInDB:
    if current_user.disabled:
        raise UserIsInactiveException

    return current_user


async def add_user(
        user_data: UserDuringRegistration
) -> None:
    existing_user = await UserDAO.find_one_or_none(
        name=user_data.name
    )

    if existing_user:
        raise UserAlreadyExistsException

    hashed_password = get_password_hash(user_data.password)

    new_user = await UserDAO.add(
        name=user_data.name,
        email=user_data.email,
        full_name=user_data.full_name,
        disabled=False,
        hashed_password=hashed_password,
    )

    if not new_user:
        raise CannotAddDataToDatabase


logger.info(msg='init users services')
