from app.core.db_base import BaseDAO
from app.core.logger import logger
from app.notes.models import Notes


class NoteDAO(BaseDAO):
    model = Notes


logger.info(msg='init notes dao')
