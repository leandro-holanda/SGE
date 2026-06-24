FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update \
    && apt install -y \
        nano \
        curl \
        gcc \
        g++ \
        python3-dev \
        libpango-1.0-0 \
        libpangoft2-1.0-0 \
        libgdk-pixbuf-2.0-0 \
        libffi-dev \
        shared-mime-info \
        libcairo2 \
        libpangocairo-1.0-0 \
        libgirepository-1.0-1 \
        gir1.2-pango-1.0 \
        pkg-config \
        libpq-dev \
        libjpeg-dev \
        zlib1g-dev \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["/bin/sh", "-c", "python manage.py collectstatic --noinput && python manage.py migrate && gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 3"]