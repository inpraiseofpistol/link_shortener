from pydantic_settings import BaseSettings

class DBConfig(BaseSettings):
    postgres_db: str = "shortener"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    postgres_host: str = "localhost"

    @property
    def conn_url(self) -> str:
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:5432/{self.postgres_db}"

class AppConfig(BaseSettings):
    base_url: str = "http://localhost:8000"