from fastapi import FastAPI, APIRouter
from app.dao.base import BaseDAO
from app.sites.dao import SitesDAO

router = APIRouter(
    prefix="/sites",
    tags=["Сайты"]
)

