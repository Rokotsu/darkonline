from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rating = Column(Float)
    image = Column(String)
    seller_id = Column(Integer, ForeignKey('users.user_id'))
    seller_image = Column(String)
    price = Column(Float)
    currency = Column(String)

    seller = relationship("User", back_populates="seller_products")
    comments = relationship("ProductComment", back_populates="product")