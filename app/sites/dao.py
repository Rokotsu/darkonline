from sqlalchemy import select
from app.dao.base import BaseDAO
from app.sites.models import Site
from app.sites.categories.models import Category
from app.database import async_session_maker
from typing import List, Dict


class SitesDAO(BaseDAO):
    model = Site

    @classmethod
    async def get_sites_with_categories(cls) -> List[dict]:
        async with async_session_maker() as session:
            query = select(Site, Category).join(Category)
            result = await session.execute(query)
            data = result.fetchall()

            sites_with_categories = []
            for site, category in data:
                site_dict = {
                    "site_id": site.site_id,
                    "site_name": site.site_name,
                    "description": site.description,
                    "recommend": site.recommend,
                    "status": site.status,
                    "category_id": site.category_id,
                    "logo_link": site.logo_link,
                    "category": category.name
                }
                sites_with_categories.append(site_dict)

            return sites_with_categories



