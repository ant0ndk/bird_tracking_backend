from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import Float, Integer, String
from sqlalchemy.dialects.postgresql import JSONB


class Base(DeclarativeBase):
    pass


class SensorMessage(Base):
    __tablename__ = "sensor_messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    device_id: Mapped[str] = mapped_column(String(24), index=True)
    timestamp: Mapped[int] = mapped_column(Integer, index=True)
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    data: Mapped[dict] = mapped_column(JSONB)  # все остальные поля
