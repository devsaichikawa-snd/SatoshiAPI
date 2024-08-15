import json
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from config.logger import log_decorator
from db.db_settings import get_db
from db.crud import get_select_all
from db.publicGym_crud import get_select as get_publicGym_select
from db.snd_crud import get_select as get_snd_select
from models.snd_model import SndBroadcast
from models.public_gym_model import PublicGym
from schemas.snd_schema import SndBroadcastRequest, SndBroadcastResponse
from schemas.public_gym_schema import PublicGymRequest, PublicGymResponse
from src.data_import import import_snd_data, import_publicGym_data
from src.gym_webscraping import web_scraping
from src.gym_data_cleansing import data_cleansing


app = FastAPI()

TABLE_DICT = {
    "public_gym": PublicGym,
    "snd_broadcast": SndBroadcast,
}


@log_decorator
@app.get("/satoshiApi/")
def snd_root():
    """"""
    url_dict = {
        "select_ALL": "/(table_nameを入れて)/",
        "snd_select": "/snd_select/",
        "public_gym_select": "/public_gym_select/",
    }

    return url_dict


@log_decorator
@app.get("/satoshiApi/{table_name}/")
def select_all(table_name, db: Session = Depends(get_db)):
    """"""
    result = get_select_all(db, TABLE_DICT[table_name])

    return result


@log_decorator
@app.get("/satoshiApi/snd_select/", response_model=SndBroadcastResponse)
def snd_select(
    param_where: SndBroadcastRequest,
    param_orderby,
    param_limit,
    db: Session = Depends(get_db),
):
    """"""
    if param_where:
        where: SndBroadcastRequest = json.loads(param_where)
    if param_orderby:
        orderby = json.loads(param_orderby)
    if param_limit:
        limit = param_limit
    result = get_snd_select(db, SndBroadcast, where, orderby, limit)

    return result


@log_decorator
@app.get("/public_gym/public_gym_select/", response_model=PublicGymResponse)
def public_gym_select(
    param_where: PublicGymRequest,
    param_orderby,
    param_limit,
    db: Session = Depends(get_db),
):
    """"""
    if param_where:
        where: PublicGymRequest = json.loads(param_where)
    if param_orderby:
        orderby = json.loads(param_orderby)
    if param_limit:
        limit = param_limit
    result = get_publicGym_select(db, PublicGym, where, orderby, limit)

    return result


def __inport_snd_data_controller():
    """SNDの集計ファイルを取り込む"""
    import_snd_data()


def __inport_gym_controller():
    """公共体育館のデータ収集および集計ファイルの取り込み"""
    gym_list = web_scraping()
    if gym_list:
        data_cleansing(gym_list)
    else:
        print("gym_listがありません。")
    import_publicGym_data()


if __name__ == "__main__":
    print("Hello SATOSHI!")
    # __inport_snd_data_controller()
    # __inport_gym_controller()
