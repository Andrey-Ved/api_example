from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Union

from app.core.logger import logger


class Note(BaseModel):
    create_at: Union[datetime, None] = None
    text: str

    model_config = ConfigDict(from_attributes=True)


logger.info(msg='init notes schemas')
