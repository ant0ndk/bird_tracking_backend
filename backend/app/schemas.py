from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class SensorVersionCreate(BaseModel):
    version: str

class SensorCreate(BaseModel):
    internal_id: str
    name: str
    version: str

class BirdCreate(BaseModel):
    bird_name: str

class SensorDataCreate(BaseModel):
    timestamp: datetime # ISO 8601 standart YYYY-MM-DDTHH:MM:SSZ
    is_light: bool
    latitude: float
    longitude: float
    internal_id: str

class CoordinateResponse(BaseModel):
    latitude: float
    longitude: float
    timestamp: datetime
