from app.database import Base
from sqlalchemy import Column, String, Integer, Text, DateTime


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(DateTime)
    text = Column(String, nullable=False)
    views = Column(Integer, nullable=False)