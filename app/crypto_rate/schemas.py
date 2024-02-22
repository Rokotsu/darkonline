from pydantic import BaseModel

class SCryptoRate(BaseModel):
    id: int
    name: str
    value: float
    image: str