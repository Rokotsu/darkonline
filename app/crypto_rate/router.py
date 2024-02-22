from fastapi import APIRouter
from app.crypto_rate.dao import CryptoRateDAO

from app.crypto_rate.schemas import SCryptoRate

router = APIRouter(
    prefix="/crypto_rate",
    tags=["Криптовалюты"],
)

@router.get("")
async def get_crypto_rate() -> list[SCryptoRate]:
    return await CryptoRateDAO.find_all()