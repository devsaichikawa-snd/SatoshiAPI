from pydantic import BaseModel


class PublicGymBase(BaseModel):
    """PublicGym Base"""

    facility_name: str | None  # 施設名称
    prefecture: str | None  # 都道府県
    municipality: str | None  # 自治体(区市町村)
    address: str | None  # 所在地
    telephone: str | None  # 電話番号
    url: str | None  # HP-URL
    training_room_flag: str | None  # トレーニングルームの有無


class PublicGymRequest(PublicGymBase):
    """PublicGym Request

    validationとserialize/deserializeを担当する
    """

    pass


class PublicGymResponse(PublicGymBase):
    """PublicGym Response

    validationとserialize/deserializeを担当する
    """

    id: int

    class Config:
        from_attributes = True
