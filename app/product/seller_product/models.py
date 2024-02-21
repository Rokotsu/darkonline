from sqlalchemy import  Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class SellerProduct(Base):
    __tablename__ = 'seller_products'

    id = Column(Integer, primary_key=True)
    seller_id = Column(Integer, ForeignKey('users.user_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))

    seller = relationship("User", back_populates="seller_products")
    product = relationship("Product", back_populates="seller_products")