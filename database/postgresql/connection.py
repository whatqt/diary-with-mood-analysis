from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs
from os import getenv



CONNECTION_URL = f"postgresql+asyncpg://postgres:{getenv("PASSWORD_POSTGRES")}@localhost/diary_with_mood_analysis"

engine = create_async_engine(
    url=CONNECTION_URL,
    echo=True
)





