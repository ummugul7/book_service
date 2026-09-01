FROM python:3.11-slim

WORKDIR /app

# Sistem bağımlılıkları ve temizlik
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Uygulama portu
EXPOSE 8000

# Uvicorn ile başlat (Tüm arayüzleri dinleyecek şekilde)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]