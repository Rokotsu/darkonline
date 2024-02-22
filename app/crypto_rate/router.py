from fastapi import APIRouter
from app.crypto_rate.dao import CryptoRateDAO

from app.crypto_rate.schemas import SCryptoRateInfo

router = APIRouter(
    prefix="/crypto_rate",
    tags=["Криптовалюты"],
)

@router.get("")
async def get_crypto_rate() -> list[SCryptoRateInfo]:
    return await CryptoRateDAO.find_all()