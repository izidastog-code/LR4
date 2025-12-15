FROM python:3.11-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код сервиса
COPY request_generator.py .

# Команда запуска
CMD ["python", "request_generator.py"]
