FROM python:3.11-slim

# Установка зависимостей
WORKDIR /app

COPY infra/backend_requirements.txt /app/backend_requirements.txt
RUN pip install --no-cache-dir -r backend_requirements.txt

# Копируем всё приложение

COPY /backend /app
COPY infra/.env /app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# uvicorn app.main:app --host=0.0.0.0 --port=8000
