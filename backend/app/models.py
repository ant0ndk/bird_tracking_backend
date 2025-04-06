from datetime import datetime

from app.database import Base
from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import relationship


class SensorVersion(Base):
    __tablename__ = "sensor_versions"
    id = Column(Integer, primary_key=True, index=True)
    version = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    internal_id = Column(String, unique=True, index=True)
    version_id = Column(Integer, ForeignKey("sensor_versions.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    version = relationship("SensorVersion")

class Bird(Base):
    __tablename__ = "birds"
    id = Column(Integer, primary_key=True, index=True)
    bird_name = Column(String, unique=True)

class SensorData(Base):
    __tablename__ = "sensor_data"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    is_light = Column(Boolean)
    latitude = Column(Float)
    longitude = Column(Float)
    sensor_id = Column(Integer, ForeignKey("sensors.id"))

    sensor = relationship("Sensor")
