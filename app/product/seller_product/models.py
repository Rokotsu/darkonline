from sqlalchemy import  Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Seller(Base):
    __tablename__ = 'sellers'

    id = Column(Integer, primary_key=True)
    seller_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))

    seller = relationship("User", back_populates="seller_products")
    product = relationship("Product", back_populates="seller_products")