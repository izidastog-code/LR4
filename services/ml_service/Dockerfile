FROM python:3.11-slim

# Рабочая директория внутри контейнера
WORKDIR /ml_service

# Копируем всё содержимое папки ml_service внутрь контейнера
COPY . /ml_service

# Делаем директорию /models volume-ом (туда смонтируем модель)
VOLUME ["/models"]

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Порт сервиса
EXPOSE 8000

# Команда запуска сервера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# ---------------------------
# Команда сборки образа (из папки services/ml_service):
# docker build -t heart-ml-service:1 .
#
# Команда запуска контейнера:
# docker run --rm -p 8000:8000 -v $(pwd)/../models:/models heart-ml-service:1
# ---------------------------
