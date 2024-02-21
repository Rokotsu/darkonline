from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Site(Base):
    __tablename__ = 'sites'

    site_id = Column(Integer, primary_key=True)
    site_name = Column(String, nullable=False)
    description = Column(Text)
    recommend = Column(Boolean)
    status = Column(Boolean)
    category_id = Column(Integer, ForeignKey('categories.id'))
    logo_link = Column(String)

    category = relationship("Category", back_populates="sites")
    comments = relationship("SiteComment", back_populates="site")