from app.database import SessionLocal
from app.models import Bird


def init_birds():
    birds = ["Соловей", "Ласточка", "Синица", "Грач", "Скворец"]
    db = SessionLocal()
    for bird in birds:
        if not db.query(Bird).filter_by(bird_name=bird).first():
            db.add(Bird(bird_name=bird))
    db.commit()
    db.close()
