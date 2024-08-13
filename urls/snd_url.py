import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.logger import log_decorator
from db.snd_crud import get_select_all, get_select
from db.db_settings import get_db
from models.snd_model import SndBroadcast
from schemas.snd_schema import SndBroadcastRequest, SndBroadcastResponse


snd_router = APIRouter()


@log_decorator
@snd_router.get("/snd_broadcast/")
def snd_root():
    """"""
    url_dict = {
        "snd_select_all": "/snd_select_all/",
        "snd_select": "/snd_select/",
    }

    return url_dict


@log_decorator
@snd_router.get(
    "/snd_broadcast/snd_select_all/", response_model=SndBroadcastResponse
)
def snd_select_all(db: Session = Depends(get_db)):
    """"""
    result = get_select_all(db, SndBroadcast)

    return result


@log_decorator
@snd_router.get(
    "/snd_broadcast/snd_select/", response_model=SndBroadcastResponse
)
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
    result = get_select(db, SndBroadcast, where, orderby, limit)

    return result
