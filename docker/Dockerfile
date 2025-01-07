FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=high_traffic_backend.settings

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "high_traffic_backend.wsgi:application"]