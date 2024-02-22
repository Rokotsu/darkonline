from pydantic import BaseModel

class SCryptoRateInfo(BaseModel):
    id: int
    name: str
    value: float
    image: str