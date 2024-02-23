from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    visible_nick = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    product_comments = relationship('ProductComment', back_populates='author_name')
    site_comments = relationship('SiteComment', back_populates='author_name')
    sellers = relationship('Seller', back_populates='seller')
