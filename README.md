# Bird Tracking Service

Этот сервис предназначен для отслеживания данных сенсоров и информации о птицах. Он предоставляет API для работы с данными о сенсорах, версиях сенсоров, данных с сенсоров, а также для управления записями о птицах.

## Стек технологий

- *FastAPI* — веб-фреймворк для построения API.
- *PostgreSQL* — база данных для хранения информации о сенсорах, версиях и данных с сенсоров.
- *SQLAlchemy* — ORM для взаимодействия с базой данных.
- *Docker* — для контейнеризации и удобного запуска приложения.
  
## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/ant0ndk/bird_tracking_backend.git
cd bird-tracking-service
```

### 2. Настройка переменных окружения
В папке infra создайте файл .env и добавьте в него следующие переменные:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bird_tracking_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
APP_HOST=0.0.0.0
APP_PORT=8000
```
Образец переменных окружения лежит в файле infra/.env_example

### 3. Запуск с использованием Docker Compose
```bash
docker-compose up --build
```
Эти команды соберут контейнеры, создадут сеть и запустят сервисы.
- База данных будет доступна по адресу localhost:5432.
- FastAPI сервис будет доступен по адресу http://localhost:8000/docs/



## API Документация
Документация API доступна через Swagger UI.

### Эндпоинты

#### 1. POST: Добавить запись о версии сенсора
* URL: /sensor_versions

Тело запроса:
```json
{
  "version": "1.0.0"
}
```

Ответ:
```json
{
  "id": 1,
  "version": "1.0.0",
  "created_at": "2025-04-06T12:00:00Z"
}
```

#### 2. POST: Добавить сенсор
* URL: /sensors

Тело запроса:

```json
{
  "name": "Sensor 1",
  "internal_id": "sensor_001",
  "sensor_version_id": 1
}
```

Ответ:
```json
{
  "id": 1,
  "name": "Sensor 1",
  "internal_id": "sensor_001",
  "sensor_version_id": 1,
  "created_at": "2025-04-06T12:00:00Z"
}
```
#### 3. POST: Добавить птицу
* URL: /birds

Тело запроса:
```json
{
  "name": "Eagle"
}
```

Ответ:
```json
{
  "id": 1,
  "name": "Eagle"
}
```


#### 4. POST: Добавить данные с сенсора
* URL: /sensor_data

Тело запроса:

```json
{
  "light": true,
  "latitude": 40.7128,
  "longitude": -74.0060,
  "sensor_id": 1
}
```

Ответ:
```json
{
  "id": 1,
  "light": true,
  "latitude": 40.7128,
  "longitude": -74.0060,
  "sensor_id": 1,
  "timestamp": "2025-04-06T12:00:00Z"
}
```
#### 5. GET: Получить данные о версиях сенсоров
* URL: /sensor_versions

Параметры:
```
limit: (опционально) Количество записей, которые нужно вернуть (по умолчанию 10).
```

Ответ:
```json
[
  {
    "id": 1,
    "version": "1.0.0",
    "created_at": "2025-04-06T12:00:00Z"
  },
  {
    "id": 2,
    "version": "1.1.0",
    "created_at": "2025-04-06T13:00:00Z"
  }
]
```
#### 6. GET: Получить данные о сенсорах
* URL: /sensors

Параметры:
```
limit: (опционально) Количество записей, которые нужно вернуть (по умолчанию 10).
```
Ответ:

```json
[
  {
    "id": 1,
    "name": "Sensor 1",
    "internal_id": "sensor_001",
    "sensor_version_id": 1,
    "created_at": "2025-04-06T12:00:00Z"
  }
]
```

#### 7. GET: Получить данные о птицах
* URL: /birds

Параметры:
```
limit: (опционально) Количество записей, которые нужно вернуть (по умолчанию 10).
```

Ответ:
```json
[
  {
    "id": 1,
    "name": "Eagle"
  }
]
```


#### 8. GET: Получить данные с сенсора
* URL: /sensor_data

Параметры:
```
limit: (опционально) Количество записей, которые нужно вернуть (по умолчанию 10).
```

Ответ:
```json
[
  {
    "id": 1,
    "light": true,
    "latitude": 40.7128,
    "longitude": -74.0060,
    "sensor_id": 1,
    "timestamp": "2025-04-06T12:00:00Z"
  }
]
```

### Лицензия
Этот проект лицензирован под лицензией MIT.

См. файл LICENSE для подробностей.