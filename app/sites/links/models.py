from sqlalchemy import Column, ForeignKey, String, Integer, Float, Boolean
from sqlalchemy.orm import relationship

from app.database import Base


class SiteLink(Base):
    __tablename__ = 'site_links'

    id = Column(Integer, primary_key=True)
    site_id = Column(Integer, ForeignKey('sites.id'))
    domain = Column(String, nullable=False)
    status = Column(Boolean)
    response_time = Column(Float)

    site = relationship("Site", back_populates="links")