from app.database import get_db
from app.models import SensorVersion
from app.schemas import SensorVersionCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(prefix="/sensor-version", tags=["Sensor Version"])


@router.post("/create")
def create_sensor_version(version_data: SensorVersionCreate, db: Session = Depends(get_db)):
    version = SensorVersion(version=version_data.version)
    db.add(version)
    db.commit()
    return {"status": "ok"}

@router.get("/get_data")
async def get_sensor_versions(limit: int = 10, db: Session = Depends(get_db)):
    sensor_versions = db.query(SensorVersion).limit(limit).all()
    return sensor_versions
