FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/order_system

ENV ENV_FOR_DYNACONF=production

EXPOSE 8000

CMD ["uvicorn", "admin.asgi:application", "--host", "0.0.0.0", "--port", "8000"]