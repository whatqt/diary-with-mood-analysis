from sqlalchemy import create_engine
from os import getenv



CONNECTION_URL = f"postgresql://postgres:{getenv("PASSWORD_POSTGRES")}@localhost/diary_with_mood_analysis"

engine = create_engine(
    url=CONNECTION_URL,
    echo=True
)





