from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import String, Integer, DateTime


class Base(DeclarativeBase):
    pass


class SndBroadcast(Base):
    """SndBroadcast Model"""

    __tablename__ = "snd_broadcast"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    # 放送日YYYYmmdd
    broadcast_date: Mapped[str] = mapped_column(String(8), unique=True)
    # 放送年yyyy
    broadcast_year: Mapped[str] = mapped_column(String(4), nullable=True)
    # 放送月mm
    broadcast_month: Mapped[str] = mapped_column(String(2), nullable=True)
    # 放送内容
    broadcast_content: Mapped[str] = mapped_column(String(400), nullable=True)
    # アシスタント1
    assistant_1: Mapped[str] = mapped_column(String(400), nullable=True)
    # アシスタント2
    assistant_2: Mapped[str] = mapped_column(String(400), nullable=True)
    guests: Mapped[str] = mapped_column(String(400), nullable=True)  # ゲスト
    remarks: Mapped[str] = mapped_column(String(400), nullable=True)  # 備考
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "broadcast_year": self.broadcast_year,
            "broadcast_month": self.broadcast_month,
            "broadcast_date": self.broadcast_date,
            "broadcast_content": self.broadcast_content,
            "assistant_1": self.assistant_1,
            "assistant_2": self.assistant_2,
            "guests": self.guests,
            "remarks": self.remarks,
        }
