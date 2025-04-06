from app.database import get_db
from app.models import Sensor, SensorVersion
from app.schemas import SensorCreate
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/sensors", tags=["Sensors"])


@router.post("/create")
def create_sensor(sensor_data: SensorCreate, db: Session = Depends(get_db)):
    version = db.query(SensorVersion).filter_by(version=sensor_data.version).first()
    if not version:
        raise HTTPException(status_code=404, detail="Sensor version not found")
    
    sensor = Sensor(
        internal_id=sensor_data.internal_id,
        name=sensor_data.name,
        version=version
    )
    db.add(sensor)
    db.commit()
    return {"status": "Sensor added"}


@router.get("/sensors")
async def get_sensors(limit: int = 10, db: Session = Depends(get_db)):
    sensors = db.query(Sensor).limit(limit).all()
    return sensors
