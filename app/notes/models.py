from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db_base import Base
from app.core.logger import logger


class Notes(Base):
    __tablename__ = 'notes'  # noqa

    id = Column(Integer, primary_key=True, nullable=False)
    create_at = Column(TIMESTAMP, nullable=False)
    text = Column(String, nullable=False)
    user_id = Column(ForeignKey("users.id"))

    user = relationship("Users", back_populates="notes")

    def __str__(self):
        return f"User {self.user_id} at " \
               f"{self.create_at.strftime('%Y.%m.%d')}"


logger.info(msg='init notes models')
