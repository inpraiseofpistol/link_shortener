from sqlalchemy import select
from app.entities import User
from app.tables import users
from .base import BaseAlchemyRepository

class UserRepository(BaseAlchemyRepository):
    async def get_by_email(self, email: str) -> User | None:
        res = await self.session.execute(select(users).where(users.c.email == email))
        if row := res.first():
            return User(id=row[0], email=row[1], password_hash=row[2])
        return None

    async def create(self, user: User) -> User:
        stmt = users.insert().values(email=user.email, password_hash=user.password_hash).returning(users.c.id)
        res = await self.session.execute(stmt)
        user.id = res.scalar_one()
        await self.session.flush()
        return user