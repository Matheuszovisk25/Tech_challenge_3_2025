from pydantic_settings import BaseSettings
from sqlalchemy.orm import declarative_base

DBBaseModel = declarative_base()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:admin@localhost:5432/techchallenge_db"
    #DB_URL: str = "postgresql+asyncpg://db_certo:xLkY0nQ26QTGvEUA2nGsw98rWrgeMETB@dpg-d3i88k2dbo4c73fgrf3g-a.oregon-postgres.render.com/db_certo_gddh"
    JWT_SECRET_KEY: str = '136758cdc7f7e5f1a542c736994e66fc'
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 1 semana

    class Config:
        case_sensitive = True

settings = Settings()


#import secrets
#token: str = secrets.token_urlsafe(32)
