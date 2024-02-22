from collections import defaultdict
from typing import List, Dict

from fastapi import APIRouter

from app.sites.schemas import SSite
from app.sites.dao import SitesDAO

router = APIRouter(
    prefix="/site",
    tags=['Сайты']
)


@router.get('/all')
async def get_sites_with_categories() -> Dict[str, List[SSite]]:
    sites_with_categories = await SitesDAO.get_sites_with_categories()

    #словарь, в котором ключами являются названия категорий, а значениями - списки сайтов для каждой категории
    categorized_sites = defaultdict(list)
    for site in sites_with_categories:
        category_name = site.pop("category")  # Извлекаем название категории из словаря сайта
        categorized_sites[category_name].append(SSite(**site))  # Добавляем сайт в список для соответствующей категории

    return categorized_sites
