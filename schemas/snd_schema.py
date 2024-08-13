from pydantic import BaseModel


class SndBroadcastBase(BaseModel):
    """SndBroadcast Base"""

    broadcast_date: str | None  # 放送日YYYYmmdd
    broadcast_year: str | None  # 放送年yyyy
    broadcast_month: str | None  # 放送月mm
    broadcast_content: str | None  # 放送内容
    assistant_1: str | None  # アシスタント1
    assistant_2: str | None  # アシスタント2
    guests: str | None  # ゲスト
    remarks: str | None  # 備考


class SndBroadcastRequest(SndBroadcastBase):
    """SndBroadcast Request

    validationとserialize/deserializeを担当する
    """

    pass


class SndBroadcastResponse(SndBroadcastBase):
    """SndBroadcast Response

    validationとserialize/deserializeを担当する
    """

    id: int

    class Config:
        from_attributes = True
