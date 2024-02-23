from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

from app.dao.base import BaseDAO
from app.sites.models import Site
from app.database import async_session_maker


class SitesDAO(BaseDAO):
    model = Site

    @classmethod
    async def get_all_sites(cls):
        async with async_session_maker() as session:
            # Выбираем все сайты и загружаем связанные данные
            result = await session.execute(
                select(Site).options(
                    selectinload(Site.category),
                    selectinload(Site.links)
                )
            )
            sites = result.scalars().all()

            # Форматируем данные в нужный формат
            formatted_sites = {}
            for site in sites:
                category_name = site.category.name
                if category_name not in formatted_sites:
                    formatted_sites[category_name] = []

                formatted_site = {
                    "site_id": site.site_id,
                    "site_name": site.site_name,
                    "description": site.description,
                    "links": [
                        {
                            "domain": link.domain,
                            "status": link.status,
                            "response_time": link.response_time
                        } for link in site.links
                    ],
                    "recommend": site.recommend,
                    "category": site.category_id,
                    "logo_link": site.logo_link
                }
                formatted_sites[category_name].append(formatted_site)

            return formatted_sites