from app.database import Base
from sqlalchemy import Column, String, Integer, Text, DateTime


class News(Base):
    __tablename__ = 'news'

    news_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(DateTime)
    text = Column(Text)
    views = Column(Integer)