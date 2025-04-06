from app.database import Base, engine
from app.init_data import init_birds
from app.routers import birds, sensor_data, sensor_versions, sensors
from fastapi import FastAPI

app = FastAPI(title="Bird Tracking Service")

# Создание таблиц при первом запуске
Base.metadata.create_all(bind=engine)

# Инициализация таблицы птиц
@app.on_event("startup")
def on_startup():
    init_birds()

# Регистрация роутеров
app.include_router(sensor_versions.router)
app.include_router(sensors.router)
app.include_router(birds.router)
app.include_router(sensor_data.router)
