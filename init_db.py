"""各プロジェクトにおいて、MySQLにテーブルを作成したいときに、単体でこのファイル実行すること
コマンド: python init_db.py
"""

from db.db_settings import get_db_engine
from models.snd_model import Base, SndBroadcast
from models.public_gym_model import Base, PublicGym


def init_db_all():
    """テーブル作成を実行する"""
    engine = get_db_engine()
    # Drop Table All
    Base.metadata.drop_all(engine)
    # Create Table All
    Base.metadata.create_all(engine)


def init_db(tables_to_create=None, tables_to_drop=None):
    """指定したテーブルを作成または削除する"""
    engine = get_db_engine()

    # 指定されたテーブルのみ削除
    if tables_to_drop:
        for table in tables_to_drop:
            table.__table__.drop(engine)

    # 指定されたテーブルのみ作成
    if tables_to_create:
        for table in tables_to_create:
            table.__table__.create(engine)


if __name__ == "__main__":
    # init_db_all()
    init_db(tables_to_create=[PublicGym], tables_to_drop=[PublicGym])
