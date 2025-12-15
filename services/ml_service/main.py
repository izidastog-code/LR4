# services/ml_service/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import (
    Counter,
    Histogram,
    generate_latest,
    CONTENT_TYPE_LATEST,
)
from starlette.responses import Response

# =========================
# Prometheus metrics
# =========================

REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "path", "status_code"],
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency (seconds)",
    ["method", "path"],
)

PREDICTIONS_HIST = Histogram(
    "model_predictions",
    "Histogram of model predictions",
    buckets=(-50, -10, -1, 0, 1, 10, 50, 100, 200, 500, 1000),
)

# =========================
# FastAPI app
# =========================

app = FastAPI(
    title="Heart Disease Prediction Service",
    description="LR4: сервис предсказаний + Prometheus метрики",
    version="0.2.0",
)


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


# =========================
# Schemas
# =========================

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


# =========================
# API
# =========================

@app.post("/api/prediction")
async def predict(item_id: int, features: HeartFeatures):
    # latency metric for this endpoint
    with REQUEST_LATENCY.labels(method="POST", path="/api/prediction").time():
        # Заглушка предсказания (позже заменишь на модель)
        pred = float(sum(features.model_dump().values()))

        # prediction histogram
        PREDICTIONS_HIST.observe(pred)

        # request counter (успех)
        REQUESTS_TOTAL.labels(method="POST", path="/api/prediction", status_code="200").inc()

        return {"item_id": item_id, "predict": pred}


# =========================
# Count errors automatically
# =========================

@app.middleware("http")
async def count_all_requests(request, call_next):
    # чтобы ловить 4xx/5xx и считать их метрикой
    with REQUEST_LATENCY.labels(method=request.method, path=request.url.path).time():
        response = await call_next(request)

    REQUESTS_TOTAL.labels(
        method=request.method,
        path=request.url.path,
        status_code=str(response.status_code),
    ).inc()

    return response
