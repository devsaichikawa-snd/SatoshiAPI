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
    pGym_dict = [pGym.to_dict() for pGym in results]

    if as_json:
        # jsonにする場合
        pGym_json = json.dumps(pGym_dict, indent=2)
        return pGym_json

    return pGym_dict


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
        where_stmt = __create_public_gym_where(where)

    # ORDER BYの生成
    orderby_stmt = []
    if orderby:
        orderby_stmt = __create_public_gym_orderby(orderby)

    # クエリを作成する
    stmt = (
        select(table).where(*where_stmt).order_by(*orderby_stmt).limit(limit)
    )

    # クエリを実行する
    results = db.execute(stmt).scalars().all()

    # python object → dict in list
    public_gym_dict = [public_gym.to_dict() for public_gym in results]

    if as_json:
        # jsonにする場合
        public_gym_json = json.dumps(public_gym_dict, indent=2)
        return public_gym_json

    return public_gym_dict


def __create_public_gym_where(where):
    """"""
    where_stmt = []

    if "facility_name" in where.keys():
        where_stmt.append(column("facility_name") == where["facility_name"])
    if "prefecture" in where.keys():
        where_stmt.append(column("prefecture") == where["prefecture"])
    if "municipality" in where.keys():
        where_stmt.append(column("municipality") == where["municipality"])
    if "address" in where.keys():
        where_stmt.append(column("address") == where["address"])
    if "telephone" in where.keys():
        where_stmt.append(column("telephone") == where["telephone"])
    if "url" in where.keys():
        where_stmt.append(column("url") == where["url"])
    if "training_room_flag" in where.keys():
        where_stmt.append(
            column("training_room_flag") == where["training_room_flag"]
        )

    return where_stmt


def __create_public_gym_orderby(orderby):
    """"""
    orderby_stmt = []

    if "facility_name" in orderby.keys():
        orderby_stmt.append(
            column("facility_name") == orderby["facility_name"]
        )
    if "prefecture" in orderby.keys():
        orderby_stmt.append(column("prefecture") == orderby["prefecture"])
    if "municipality" in orderby.keys():
        orderby_stmt.append(column("municipality") == orderby["municipality"])
    if "address" in orderby.keys():
        orderby_stmt.append(column("address") == orderby["address"])
    if "telephone" in orderby.keys():
        orderby_stmt.append(column("telephone") == orderby["telephone"])
    if "url" in orderby.keys():
        orderby_stmt.append(column("url") == orderby["url"])
    if "training_room_flag" in orderby.keys():
        orderby_stmt.append(
            column("training_room_flag") == orderby["training_room_flag"]
        )

    return orderby_stmt
