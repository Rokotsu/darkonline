from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.database import Base


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    visible_nick = Column(String)
    password = Column(String, nullable=False)

    site_comments = relationship("SiteComment", back_populates="author")
    product_comments = relationship("ProductComment", back_populates="author")
