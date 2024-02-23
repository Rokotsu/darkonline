from sqlalchemy import String, Integer, DateTime, ForeignKey, Column, Text
from sqlalchemy.orm import relationship

from app.database import Base


class SiteComment(Base):
    __tablename__ = 'site_comments'

    id = Column(Integer, primary_key=True)
    site_id = Column(Integer, ForeignKey('sites.id'))
    author = Column(Integer, ForeignKey('users.id'))
    comment = Column(String, nullable=False)
    date = Column(DateTime)
    status = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    user_agent = Column(String, nullable=False)

    site = relationship("Site", back_populates="comments")
    author_name = relationship('User', back_populates="site_comment")