from sqlalchemy import String, Integer, DateTime, ForeignKey, Column, Text
from sqlalchemy.orm import relationship

from app.database import Base


class SiteComment(Base):
    __tablename__ = 'site_comments'

    comment_id = Column(Integer, primary_key=True)
    site_id = Column(Integer, ForeignKey('sites.site_id'))
    author = Column(String)
    comment = Column(Text)
    date = Column(DateTime)
    status = Column(String)
    ip_address = Column(String)
    user_agent = Column(String)

    site = relationship("Site", back_populates="comments")