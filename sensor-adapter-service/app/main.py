from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.http_endpoints import router as http_router
from app.core.database import start_database
from app.config.settings import settings
import asyncio

app = FastAPI(title="Sensor Adapter Service")

app.include_router(http_router, prefix="/api/v1")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await start_database()    

# --- TCP server -----------------------------------------------------------
if settings.ENABLE_TCP_SERVER:
    from app.api.tcp_server import run_tcp_server

    @asynccontextmanager
    async def tcp_lifespan(app: FastAPI):
        loop = asyncio.get_event_loop()
        loop.create_task(run_tcp_server(settings.APP_HOST, settings.APP_TCP_PORT))
