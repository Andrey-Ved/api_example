from pydantic import BaseModel, EmailStr, ConfigDict

from app.core.logger import logger


class User(BaseModel):
    name: str
    email: EmailStr
    full_name: str | None = None
    disabled: bool = False

    model_config = ConfigDict(from_attributes=True)


class UserDuringRegistration(User):
    password: str


class UserInDB(User):
    id: int
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


logger.info(msg='init users schemas')
