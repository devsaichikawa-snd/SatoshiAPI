import json
from fastapi import FastAPI

from db.db_settings import get_db_session
from db.crud import get_select_all, get_select
from models.snd_model import SndBroadcast
from schemas.snd_schema import SndBroadcastRequest, SndBroadcastResponse
from views.snd_data_inport import import_data


app = FastAPI()
db = get_db_session()


@app.get("/")
def root():
    url_dict = {
        "snd_select_all": "/snd_select_all/",
        "snd_select": "/snd_select/",
    }
    return url_dict


@app.get("/snd_select_all/", response_model=SndBroadcastResponse)
def snd_select_all():
    result = get_select_all(db, SndBroadcast)
    return result


@app.get("/snd_select/", response_model=SndBroadcastResponse)
def snd_select(param_where: SndBroadcastRequest, param_orderby, param_limit):
    if param_where:
        where: SndBroadcastRequest = json.loads(param_where)
    if param_orderby:
        orderby = json.loads(param_orderby)
    if param_limit:
        limit = param_limit
    result = get_select(db, SndBroadcast, where, orderby, limit)
    return result


if __name__ == "__main__":
    print("Hello")
    # import_data()
