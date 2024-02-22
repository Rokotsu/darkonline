from app.crypto_rate.models import CryptoRate
from app.dao.base import BaseDAO



class CryptoRateDAO(BaseDAO):
    model = CryptoRate

