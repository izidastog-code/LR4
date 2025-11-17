Лабораторная работа №3
Разработка микросервиса предсказаний на FastAPI с использованием Docker
1. Цель работы

Создать микросервис, выполняющий предсказания обученной модели машинного обучения.
Сервис должен предоставлять REST API, использовать модель, выгруженную из MLflow, и быть упакован в Docker-контейнер.

2. Структура проекта
my_proj
│
├── services
│   ├── ml_service
│   │   ├── main.py
│   │   ├── api_handler.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   │
│   └── models
│       ├── get_model.py
│       └── model.pkl
│
├── requirements.txt
├── .gitignore
└── README.md

3. Установка и подготовка окружения
3.1. Создание виртуального окружения
python3.13 -m venv .venv
source .venv/bin/activate

3.2. Установка зависимостей
pip install -r requirements.txt

4. Подготовка модели

Файл модели model.pkl gjkexftv из MLflow.

Команда для выгрузки модели:
python services/models/get_model.py


После выполнения в каталоге появился файл:

services/models/model.pkl

5. FastAPI сервис

Основной модуль: services/ml_service/main.py
Вспомогательный модуль: services/ml_service/api_handler.py

Доступные методы API
GET /

Возвращает тестовый ответ.

Пример:

{
  "Hello": "World"
}

POST /api/prediction?item_id=<id>



5. Локальный запуск FastAPI сервера
uvicorn services.ml_service.main:app --reload


Сервис доступен по адресам:

http://localhost:8000

http://localhost:8000/docs
 (Swagger)

6. Docker
6.1. Сборка Docker-образа
docker build -t heart-ml-service:1 .

6.2. Запуск контейнера
docker run -d \
  -p 8000:8000 \
  -v $(pwd)/../models:/models \
  --name heart-ml-container \
  heart-ml-service:1

6.3. Проверка состояния
docker ps

7. Файлы, не включаемые в репозиторий (.gitignore)
.venv/
__pycache__/
*.pyc

mlruns/
mlflow/
*.db

*.log

8. Результаты работы

В ходе лабораторной работы было выполнено:

Выгрузка обученной модели из MLflow.

Подготовка скрипта для загрузки модели в сервис.

Создание микросервиса на FastAPI.

Реализация REST-методов для предсказаний.

Создание Dockerfile.

Сборка Docker-образа.

Запуск микросервиса в Docker-контейнере.