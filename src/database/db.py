from sqlalchemy import create_engine
from .config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

def get_engine():
    url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(url)
    return engine
