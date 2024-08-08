import json
from fastapi import APIRouter

from db.crud import get_select_all, get_select
from db.db_settings import get_db
from models.snd_model import SndBroadcast
from schemas.snd_schema import SndBroadcastRequest, SndBroadcastResponse


router = APIRouter()
db = get_db()


@router.get("/snd_broadcast/")
def snd_root():
    """"""
    url_dict = {
        "snd_select_all": "/snd_select_all/",
        "snd_select": "/snd_select/",
    }

    return url_dict


@router.get(
    "/snd_broadcast/snd_select_all/", response_model=SndBroadcastResponse
)
def snd_select_all():
    """"""
    result = get_select_all(db, SndBroadcast)

    return result


@router.get("/snd_broadcast/snd_select/", response_model=SndBroadcastResponse)
def snd_select(param_where: SndBroadcastRequest, param_orderby, param_limit):
    """"""
    if param_where:
        where: SndBroadcastRequest = json.loads(param_where)
    if param_orderby:
        orderby = json.loads(param_orderby)
    if param_limit:
        limit = param_limit
    result = get_select(db, SndBroadcast, where, orderby, limit)

    return result
