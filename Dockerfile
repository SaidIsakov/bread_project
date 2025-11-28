FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    vim \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY . .


CMD ["sh", "-c", "python manage.py migrate && gunicorn reverence.wsgi.application --bind 0.0.0.0:8000"]
