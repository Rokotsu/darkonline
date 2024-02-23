from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    name = Column(String, nullable=False)
    rating = Column(Float)
    image = Column(String, nullable=False)
    seller_id = Column(Integer, ForeignKey('users.id'))
    seller_image = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    currency = Column(String, nullable=False)

    seller = relationship("User", back_populates="seller_products")
    comments = relationship("ProductComment", back_populates="product")
