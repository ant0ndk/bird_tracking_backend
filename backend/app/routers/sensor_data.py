from datetime import datetime
from typing import List, Optional

from app.database import get_db
from app.models import Sensor, SensorData
from app.schemas import CoordinateResponse, SensorDataCreate
from app.utils import calculate_avg_distance, calculate_avg_speed
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import and_
from sqlalchemy.orm import Session

router = APIRouter(prefix="/sensor-data", tags=["Sensor Data"])


@router.post("/")
def add_sensor_data(data: SensorDataCreate, db: Session = Depends(get_db)):
    sensor = db.query(Sensor).filter_by(internal_id=data.internal_id).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")

    record = SensorData(
        timestamp=data.timestamp,
        is_light=data.is_light,
        latitude=data.latitude,
        longitude=data.longitude,
        sensor=sensor
    )
    db.add(record)
    db.commit()
    return {"status": "Sensor data added"}

@router.get("/avg-speed/")
def get_avg_speed(
    internal_id: str,
    date_from: datetime,
    date_to: datetime,
    times_of_day: Optional[bool] = False,
    db: Session = Depends(get_db)
):
    sensor = db.query(Sensor).filter_by(internal_id=internal_id).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")

    query = db.query(SensorData).filter(
        SensorData.sensor_id == sensor.id,
        SensorData.timestamp >= date_from,
        SensorData.timestamp <= date_to
    )
    
    if times_of_day:
        query = query.filter(SensorData.is_light == True)

    records = query.order_by(SensorData.timestamp).all()
    avg_speed = calculate_avg_speed(records)
    return {"average_speed_kmh": avg_speed}

@router.get("/avg-distance/")
def get_avg_distance(
    internal_id: str,
    date_from: datetime,
    date_to: datetime,
    times_of_day: Optional[bool] = False,
    db: Session = Depends(get_db)
):
    sensor = db.query(Sensor).filter_by(internal_id=internal_id).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")

    query = db.query(SensorData).filter(
        SensorData.sensor_id == sensor.id,
        SensorData.timestamp >= date_from,
        SensorData.timestamp <= date_to
    )
    if times_of_day:
        query = query.filter(SensorData.is_light == True)

    records = query.order_by(SensorData.timestamp).all()
    avg_distance = calculate_avg_distance(records)
    return {"average_distance_km": avg_distance}

@router.get("/coordinates/by-sensor/", response_model=List[CoordinateResponse])
def get_coordinates_by_sensor(
    internal_id: str,
    date_from: datetime,
    date_to: datetime,
    db: Session = Depends(get_db)
):
    sensor = db.query(Sensor).filter_by(internal_id=internal_id).first()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")

    records = db.query(SensorData).filter(
        SensorData.sensor_id == sensor.id,
        SensorData.timestamp >= date_from,
        SensorData.timestamp <= date_to
    ).all()

    return [
        CoordinateResponse(
            latitude=r.latitude,
            longitude=r.longitude,
            timestamp=r.timestamp
        ) for r in records
    ]


@router.get("/get_data")
async def get_sensor_data(limit: int = 10, db: Session = Depends(get_db)):
    sensor_data = db.query(SensorData).limit(limit).all()
    return sensor_data
