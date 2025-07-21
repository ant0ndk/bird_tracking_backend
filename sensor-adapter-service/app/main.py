from fastapi import FastAPI
from app.api.http_endpoints import router as http_router
from app.config.settings import settings
import asyncio

app = FastAPI(title="Sensor Adapter Service")

app.include_router(http_router, prefix="/api/v1")

# --- TCP server -----------------------------------------------------------
if settings.ENABLE_TCP_SERVER:
    from app.api.tcp_server import run_tcp_server

    @app.on_event("startup")
    async def _start_tcp():
        loop = asyncio.get_event_loop()
        loop.create_task(run_tcp_server("0.0.0.0", 9999))
