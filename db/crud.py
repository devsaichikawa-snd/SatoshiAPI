import json
from sqlalchemy import select

from config.logger import log_decorator


@log_decorator
def get_select_all(db, table, as_json=False):
    """1テーブルから全検索する"""
    # クエリ文字列を生成する→ SELECT * FROM <table>;
    stmt = select(table)

    # クエリを実行する
    results = db.execute(stmt).scalars().all()

    # python object → dict in list
    result_dict = [result.to_dict() for result in results]

    if as_json:
        # jsonにする場合
        snd_json = json.dumps(result_dict, indent=2)
        return snd_json

    return result_dict
