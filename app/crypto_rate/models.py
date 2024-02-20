from sqlalchemy import Column, Integer, String, float, Float
from app.database import Base

class CryptoRate(Base):
    __tablename__ = 'crypto_rates'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    image = Column(String)