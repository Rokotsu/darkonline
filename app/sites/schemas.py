from pydantic import BaseModel
from typing import List, Optional

class SiteLink(BaseModel):
    domain: str
    status: int
    response_time: Optional[float]

class Site(BaseModel):
    site_id: int
    site_name: str
    description: str
    links: List[SiteLink]
    recommend: bool
    status: bool
    category: int
    logo_link: str

class SSite(BaseModel):
    category_name: List[Site]

