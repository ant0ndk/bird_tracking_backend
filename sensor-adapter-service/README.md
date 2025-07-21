# Sensor Adapter Service
Сервис‐адаптер для приёма бинарных пакетов с сенсоров, проверки CRC32, декодирования сообщений типа 0x02 и сохранения результатов в PostgreSQL. Реализованы приём по HTTP (application/octet-stream) и через TCP-сервер на отдельном порту.

### Переменные окружения
```
DATABASE_URL - строка подключения к PostgreSQL
ENABLE_TCP_SERVER - запустить/отключить TCP-сервер
```

### HTTP API
#### POST /api/v1/sensors/binary
Принимает бинарный пакет как тело запроса (Content-Type: application/octet-stream).

**Ответ 201 Created:**

```json
{
  "device_id": "0a0b0c0d0e0f101112131415",
  "saved_messages": 1
}
```
*Пример curl*
```bash
curl -X POST \
     -H "Content-Type: application/octet-stream" \
     --data-binary @packet.bin \
     http://localhost:8002/api/v1/sensors/binary
```
*TCP-протокол*
Отправьте в сокет полный бинарный пакет.
Сервер вернёт:

```text
OK <n>   # n – количество сохранённых сообщений
```
или

```text
ERR <reason>
```