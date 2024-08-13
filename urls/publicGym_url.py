import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from config.logger import log_decorator
from db.publicGym_crud import get_select_all, get_select
from db.db_settings import get_db
from models.public_gym_model import PublicGym
from schemas.public_gym_schema import PublicGymRequest, PublicGymResponse


public_gym_router = APIRouter()


@log_decorator
@public_gym_router.get("/public_gym/")
def public_gym_root():
    """"""
    url_dict = {
        "public_gym_select_all": "/public_gym_select_all/",
        "public_gym_select": "/public_gym_select/",
    }

    return url_dict


@log_decorator
@public_gym_router.get(
    "/public_gym/public_gym_select_all/", response_model=PublicGymResponse
)
def public_gym_select_all(db: Session = Depends(get_db)):
    """"""
    try:
        result = get_select_all(db, PublicGym)
    except Exception as e:
        print(e)

    return result


@log_decorator
@public_gym_router.get(
    "/public_gym/public_gym_select/", response_model=PublicGymResponse
)
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
    result = get_select(db, PublicGym, where, orderby, limit)

    return result
