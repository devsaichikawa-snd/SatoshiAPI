from dataclasses import dataclass
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import String, Integer, DateTime, Boolean


class Base(DeclarativeBase):
    pass


class PublicGym(Base):
    """PublicGym"""

    __tablename__ = "public_gym"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    # 施設名称
    facility_name = mapped_column(String(100), unique=True)
    # 都道府県
    prefecture = mapped_column(String(20))
    # 自治体(区市町村)
    municipality = mapped_column(String(20))
    # 所在地
    address = mapped_column(String(255))
    # 電話番号
    telephone = mapped_column(String(30), nullable=True)
    # HP-URL
    url = mapped_column(String(255), nullable=True)
    # トレーニングルームの有無
    training_room_flag: Mapped[bool] = mapped_column(Boolean, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "facility_name": self.facility_name,
            "prefecture": self.prefecture,
            "municipality": self.municipality,
            "address": self.address,
            "telephone": self.telephone,
            "url": self.url,
            "training_room_flag": self.training_room_flag,
        }


@dataclass
class PublicGymExcel:
    """PublicGymExcel"""

    index: int = 0
    facility_name: str = ""
    prefecture: str = ""
    municipality: str = ""
    address: str = ""
    telephone: str = ""
    url: str = ""
    training_room_flag: bool = False
