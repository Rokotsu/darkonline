from typing import List, Dict
from pydantic import BaseModel

class SSite(BaseModel):
    site_id: int
    site_name: str
    description: str
    recommend: bool
    status: bool
    category_id: int
    logo_link: str

class SResponse(BaseModel):
    category: str
    sites: List[SSite]

