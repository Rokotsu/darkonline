from sqlalchemy import Column, ForeignKey, Integer, Text, String, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class ProductComment(Base):
    __tablename__ = 'product_comments'

    comment_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    author = Column(Integer, ForeignKey('users.user_id'))
    author_avatar = Column(String, nullable=False)
    text = Column(String, nullable=False)
    date = Column(DateTime)
    stars = Column(Integer, nullable=False)

    product = relationship("Product", back_populates="comments")
    author = relationship("User", back_populates="product_comments")