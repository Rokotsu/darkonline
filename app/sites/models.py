from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from app.database import Base


class Site(Base):
    __tablename__ = 'sites'

    site_id = Column(Integer, primary_key=True, nullable=False)
    site_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    recommend = Column(Boolean)
    status = Column(Boolean)
    category_id = Column(Integer, ForeignKey('categories.id'))
    logo_link = Column(String, nullable=False)