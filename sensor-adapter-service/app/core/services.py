from typing import List, Dict
from sqlalchemy import insert
from app.core.database import engine
from app.core.models import SensorMessage


async def save_messages(device_id: str, messages: List[Dict]) -> int:
    to_insert = [
        {
            "device_id": device_id,
            "timestamp": m["timestamp"],
            "latitude": m["latitude"],
            "longitude": m["longitude"],
            "data": m,
        }
        for m in messages
    ]

    async with engine.begin() as conn:
        await conn.execute(insert(SensorMessage), to_insert)

    return len(to_insert)
