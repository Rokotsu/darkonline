from sqlalchemy import Column, String, Integer

from app.database import Base


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    visible_nick = Column(String, nullable=False)
    password = Column(String, nullable=False)
