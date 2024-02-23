from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Site(Base):
    __tablename__ = 'sites'

    id = Column(Integer, primary_key=True)
    site_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    recommend = Column(Boolean)
    category_id = Column(Integer, ForeignKey('categories.id'))
    link_id = Column(Integer, ForeignKey('site_links.id'))
    logo_link = Column(String, nullable=False)

    category = relationship("Category", back_populates="sites")
    links = relationship("SiteLink", back_populates="site")