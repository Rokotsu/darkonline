from sqlalchemy import Column, ForeignKey, String, Integer, Float
from sqlalchemy.orm import relationship

from app.database import Base


class SiteLink(Base):
    __tablename__ = 'site_links'

    link_id = Column(Integer, primary_key=True)
    site_id = Column(Integer, ForeignKey('sites.site_id'))
    domain = Column(String, nullable=False)
    status = Column(Integer, nullable=False)
    response_time = Column(Float)

    site = relationship("Site", back_populates="links")