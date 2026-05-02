from sqlalchemy import select
from app.entities import Link
from app.tables import links
from .base import BaseAlchemyRepository

class LinkRepository(BaseAlchemyRepository):
    async def create(self, link: Link) -> Link:
        stmt = links.insert().values(
            original_url=link.original_url, short_code=link.short_code,
            user_id=link.user_id, created_at=link.created_at
        ).returning(links.c.id)
        res = await self.session.execute(stmt)
        link.id = res.scalar_one()
        await self.session.flush()
        return link

    async def get_by_code(self, code: str) -> Link | None:
        res = await self.session.execute(select(links).where(links.c.short_code == code))
        if row := res.first():
            return Link(id=row[0], original_url=row[1], short_code=row[2], user_id=row[3], created_at=row[4])
        return None