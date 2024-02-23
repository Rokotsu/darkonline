from collections import defaultdict
from typing import List, Dict

from fastapi import APIRouter

from app.sites.schemas import SSite
from app.sites.dao import SitesDAO

router = APIRouter(
    prefix="/site",
    tags=['Сайты']
)


@router.get("/all")
async def get_sites() -> list[SSite]:
    return await SitesDAO.get_all_sites()
