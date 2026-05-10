from typing import AsyncGenerator
from dishka import Provider, provide, make_async_container, Scope
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
from app.config import DBConfig
from app.repositories.link import LinkRepository
from app.services.shortener import ShortenerService

class ConfigProvider(Provider):
    scope = Scope.APP

    @provide
    def db_cfg(self) -> DBConfig:
        return DBConfig()

class DBProvider(Provider):
    scope = Scope.APP

    @provide
    def engine(self, cfg: DBConfig) -> AsyncEngine:
        return create_async_engine(cfg.conn_url)

    @provide
    def sessionmaker(self, eng: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(eng, expire_on_commit=False, autoflush=False)

    @provide(scope=Scope.REQUEST)
    async def session(self, sm: async_sessionmaker[AsyncSession]) -> AsyncGenerator[AsyncSession, None]:
        async with sm() as s:
            try:
                yield s
                await s.commit()
            except Exception:
                await s.rollback()
                raise
            finally:
                await s.close()

class RepoProvider(Provider):
    scope = Scope.REQUEST
    link = provide(LinkRepository)

class SvcProvider(Provider):
    scope = Scope.REQUEST
    shortener = provide(ShortenerService)

container = make_async_container(ConfigProvider(), DBProvider(), RepoProvider(), SvcProvider())