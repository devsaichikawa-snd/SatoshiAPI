import json
from sqlalchemy import select, column

from config.logger import log_decorator


@log_decorator
def get_select_all(db, table, as_json=False):
    """1テーブルから全検索する"""
    # クエリ文字列を生成する→ SELECT * FROM <table>;
    stmt = select(table)

    # クエリを実行する
    results = db.execute(stmt).scalars().all()

    # python object → dict in list
    snd_dict = [snd.to_dict() for snd in results]

    if as_json:
        # jsonにする場合
        snd_json = json.dumps(snd_dict, indent=2)
        return snd_json

    return snd_dict


@log_decorator
def get_select(db, table, where={}, orderby={}, limit=0, as_json=False):
    """1テーブルから特定レコードを検索する

    Args:
        table(model): Model
        where(dict): {column1:value1, column2:value2...}
        orderby(dict): {column: asc, column: desc...}
        limit(int): 1000
    """
    # WHEREの生成
    where_stmt = []
    if where:
        where_stmt = __create_snd_where(where)

    # ORDER BYの生成
    orderby_stmt = []
    if orderby:
        orderby_stmt = __create_snd_orderby(orderby)

    # クエリを作成する
    stmt = (
        select(table).where(*where_stmt).order_by(*orderby_stmt).limit(limit)
    )

    # クエリを実行する
    results = db.execute(stmt).scalars().all()

    # python object → dict in list
    snd_dict = [snd.to_dict() for snd in results]

    if as_json:
        # jsonにする場合
        snd_json = json.dumps(snd_dict, indent=2)
        return snd_json

    return snd_dict


def __create_snd_where(where):
    """"""
    where_stmt = []

    if "broadcast_year" in where.keys():
        where_stmt.append(column("broadcast_year") == where["broadcast_year"])
    if "broadcast_month" in where.keys():
        where_stmt.append(
            column("broadcast_month") == where["broadcast_month"]
        )
    if "broadcast_date" in where.keys():
        where_stmt.append(column("broadcast_date") == where["broadcast_date"])
    if "broadcast_content" in where.keys():
        where_stmt.append(
            column("broadcast_content") == where["broadcast_content"]
        )
    if "assistant_1" in where.keys():
        where_stmt.append(column("assistant_1") == where["assistant_1"])
    if "assistant_2" in where.keys():
        where_stmt.append(column("assistant_2") == where["assistant_2"])
    if "guests" in where.keys():
        where_stmt.append(column("guests") == where["guests"])
    if "remarks" in where.keys():
        where_stmt.append(column("remarks") == where["remarks"])

    return where_stmt


def __create_snd_orderby(orderby):
    """"""
    orderby_stmt = []

    if "broadcast_year" in orderby.keys():
        orderby_stmt.append(
            column("broadcast_year") == orderby["broadcast_year"]
        )
    if "broadcast_month" in orderby.keys():
        orderby_stmt.append(
            column("broadcast_month") == orderby["broadcast_month"]
        )
    if "broadcast_date" in orderby.keys():
        orderby_stmt.append(
            column("broadcast_date") == orderby["broadcast_date"]
        )
    if "broadcast_content" in orderby.keys():
        orderby_stmt.append(
            column("broadcast_content") == orderby["broadcast_content"]
        )
    if "assistant_1" in orderby.keys():
        orderby_stmt.append(column("assistant_1") == orderby["assistant_1"])
    if "assistant_2" in orderby.keys():
        orderby_stmt.append(column("assistant_2") == orderby["assistant_2"])
    if "guests" in orderby.keys():
        orderby_stmt.append(column("guests") == orderby["guests"])
    if "remarks" in orderby.keys():
        orderby_stmt.append(column("remarks") == orderby["remarks"])

    return orderby_stmt
