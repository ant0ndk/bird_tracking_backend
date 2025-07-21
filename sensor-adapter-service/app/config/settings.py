from pydantic_settings import BaseSettings


class _Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://user:pass@localhost:5432/sensors_db"
    ENABLE_TCP_SERVER: bool = False

    class Config:
        env_file = ".env"


settings = _Settings()