from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Heart Disease Prediction Service",
    description="Сервис предсказаний (LR3) — пока без реальной модели",
    version="0.1.0",
)


@app.get("/")
async def root():
    """
    Тестовый endpoint для проверки, что сервис жив.
    """
    return {"Hello": "World"}


class HeartFeatures(BaseModel):
    age: float
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int


@app.post("/api/prediction")
async def predict(item_id: int, features: HeartFeatures):
    """
    Временная заглушка: просто возвращаем сумму признаков.
    Позже сюда подключим настоящую модель.
    """
    s = sum(features.dict().values())
    return {"item_id": item_id, "predict": s}
