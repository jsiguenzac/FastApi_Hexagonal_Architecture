from src.schemas.db_schema import DatabaseConfig
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

db_config = DatabaseConfig(
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    host = os.getenv('DB_HOST'),
    port = os.getenv('DB_PORT'),
    database = os.getenv('DB_NAME')
)

db_url = db_config.get_url_postgresql()

engine = create_engine(db_url, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
