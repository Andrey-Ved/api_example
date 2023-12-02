from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.core.db_base import Base
from app.core.logger import logger


class Users(Base):
    __tablename__ = 'users'  # noqa

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, nullable=False)

    notes = relationship("Notes", back_populates="user")

    def __str__(self):
        return f"User {self.name} - " \
               f"e-mail {self.email}"


logger.info(msg='init users models')
