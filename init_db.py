"""各プロジェクトにおいて、MySQLにテーブルを作成したいときに、単体でこのファイル実行すること
コマンド: python init_db.py
"""


def init_db():
    """テーブル作成を実行する"""
    from db.db_settings import get_db_engine
    from models.snd_model import Base

    engine = get_db_engine()
    # Drop Table All
    Base.metadata.drop_all(engine)
    # Create Table All
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()
