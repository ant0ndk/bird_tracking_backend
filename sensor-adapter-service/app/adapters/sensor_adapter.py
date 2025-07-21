from typing import Any, Dict
from app.adapters.binary_protocol import BinaryProtocolParser
from app.core.services import save_messages


class SensorProtocolAdapter:
    """
    Высокоуровневый адаптер: принимает бинарный пакет, проверяет,
    парсит и сохраняет сообщения в БД.
    """

    def __init__(self):
        self._parser = BinaryProtocolParser()

    async def process_packet(self, raw: bytes) -> Dict[str, Any]:
        parsed = self._parser.parse_packet(raw)
        saved = await save_messages(parsed["device_id"], parsed["messages"])
        return {"device_id": parsed["device_id"], "saved_messages": saved}
