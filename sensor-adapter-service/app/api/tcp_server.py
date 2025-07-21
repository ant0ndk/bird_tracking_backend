import asyncio
from app.adapters import adapter


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    data = await reader.read()  # читаем весь пакет
    addr = writer.get_extra_info("peername")
    response = b""

    try:
        result = await adapter.process_packet(data)
        response = f"OK {result['saved_messages']}\n".encode()
    except Exception as e:
        response = f"ERR {e}\n".encode()

    writer.write(response)
    await writer.drain()
    writer.close()
    await writer.wait_closed()
    print(f"Disconnected {addr}")


async def run_tcp_server(host: str, port: int):
    server = await asyncio.start_server(handle_client, host, port)
    async with server:
        await server.serve_forever()
