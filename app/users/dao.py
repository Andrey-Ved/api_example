from app.core.db_base import BaseDAO
from app.core.logger import logger
from app.users.models import Users


class UserDAO(BaseDAO):
    model = Users


logger.info(msg='init users dao')
