from pydantic import BaseModel


class SndBroadcastRequest(BaseModel):
    """SndBroadcast Request

    validationとserialize/deserializeを担当する
    """

    broadcast_date: str  # 放送日YYYYmmdd
    broadcast_year: str | None = None  # 放送年yyyy
    broadcast_month: str | None = None  # 放送月mm
    broadcast_content: str | None = None  # 放送内容
    assistant_1: str | None = None  # アシスタント1
    assistant_2: str | None = None  # アシスタント2
    guests: str | None = None  # ゲスト
    remarks: str | None = None  # 備考


class SndBroadcastResponse(BaseModel):
    """SndBroadcast Response

    validationとserialize/deserializeを担当する
    """

    id: int
    broadcast_date: str  # 放送日YYYYmmdd
    broadcast_year: str | None  # 放送年yyyy
    broadcast_month: str | None  # 放送月mm
    broadcast_content: str | None  # 放送内容
    assistant_1: str | None  # アシスタント1
    assistant_2: str | None  # アシスタント2
    guests: str | None  # ゲスト
    remarks: str | None  # 備考

    class Config:
        orm_mode = True
