from fastapi import HTTPException, status

from app.core.logger import logger


class ExampleException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(
            status_code=self.status_code,
            detail=self.detail,
        )


class CannotAddDataToDatabase(ExampleException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Cannot add data"


class CannotGetDataInDatabase(ExampleException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Cannot get data"


class UserAlreadyExistsException(ExampleException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"


class UnauthorizedException(ExampleException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Unauthorized"


class IncorrectNameOrPasswordException(UnauthorizedException):
    detail = "Incorrect name or password"


class TokenExpiredException(UnauthorizedException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token has expired"


class TokenAbsentException(UnauthorizedException):
    detail = "Token is missing"


class IncorrectTokenFormatException(UnauthorizedException):
    detail = "Incorrect token format"


class UserIsNotPresentException(UnauthorizedException):
    detail = "User not present"


class UserIsInactiveException(UnauthorizedException):
    detail = "Inactive user"


logger.info(msg='init exception')
