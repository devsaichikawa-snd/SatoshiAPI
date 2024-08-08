import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker, Session


BASE_DIR = Path(__file__).resolve().parent.parent

# .envファイルを読み込む()
load_dotenv(os.path.join(BASE_DIR, ".env"))

DIALECT = os.environ.get("DIALECT")
DRIVER = os.environ.get("DRIVER")
DB_USER_NAME = os.environ.get("DB_USER_NAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
HOST = os.environ.get("DB_HOST", "localhost")
PORT = os.environ.get("DB_PORT", "3306")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
CHARSET_TYPE = "utf8"
DB_URL = f"{DIALECT}+{DRIVER}://{DB_USER_NAME}:{DB_PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}?charset={CHARSET_TYPE}"


db_engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)


def get_db_engine() -> Engine:
    """データベースエンジンを作成"""
    return db_engine


def dispose_db_engine(engine: Engine) -> None:
    """DBエンジンを破棄して接続を解放する"""
    return engine.dispose()


def get_db():
    """リクエストが来たらセッションを作成し、処理が完了したら閉じるためのDependency."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_session():
    """data_inport用"""
    return Session(db_engine)
