from sqlalchemy import select
from app.entities.link import Link
from app.tables.links import links
from .base import BaseAlchemyRepository


class LinkRepository(BaseAlchemyRepository):
    async def create(self, link: Link) -> Link:
        stmt = links.insert().values(
            original_url=link.original_url,
            short_code=link.short_code,
            created_at=link.created_at
        ).returning(links.c.id)
        res = await self.session.execute(stmt)
        link.id = res.scalar_one()
        await self.session.flush()
        return link

    async def get_by_code(self, code: str) -> Link | None:
        stmt = select(links).where(links.c.short_code == code)
        res = await self.session.execute(stmt)
        row = res.first()
        if row:
            return Link(
                original_url=row[1],
                short_code=row[2]
            )
        return None