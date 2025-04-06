from app.database import get_db
from app.models import Bird
from app.schemas import BirdCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(prefix="/birds", tags=["Birds"])

@router.post("/create")
def create_bird(bird_data: BirdCreate, db: Session = Depends(get_db)):
    bird = Bird(bird_name=bird_data.bird_name)
    db.add(bird)
    db.commit()
    return {"status": "Bird added"}

@router.get("/get_data")
async def get_birds(limit: int = 10, db: Session = Depends(get_db)):
    birds = db.query(Bird).limit(limit).all()
    return birds
