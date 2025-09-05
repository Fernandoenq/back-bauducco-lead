import os
import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

# pega variáveis do .env
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

# encode da senha (resolve caracteres especiais como aspas, $ etc.)
DB_PASS_ENCODED = urllib.parse.quote_plus(DB_PASS or "")

DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASS_ENCODED}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# se quiser, imprime só para debug (depois pode remover)
print("DATABASE_URL =>", DATABASE_URL)

# conexão SQLAlchemy
engine = create_engine(DATABASE_URL, future=True, echo=False)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    future=True,
)

class Base(DeclarativeBase):
    pass
