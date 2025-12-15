import time
import random
import os
import requests

# Адрес сервиса предсказаний
BASE_URL = os.getenv(
    "PREDICTION_SERVICE_URL",
    "http://localhost:8000"
)

PREDICTION_ENDPOINT = f"{BASE_URL}/api/prediction"

# Пример данных (адаптируй под свою модель при необходимости)
def generate_payload():
    return {
        "age": random.randint(30, 80),
        "sex": random.randint(0, 1),
        "cp": random.randint(0, 3),
        "trestbps": random.randint(90, 180),
        "chol": random.randint(150, 350),
        "fbs": random.randint(0, 1),
        "restecg": random.randint(0, 2),
        "thalach": random.randint(70, 210),
        "exang": random.randint(0, 1),
        "oldpeak": round(random.uniform(0.0, 6.0), 1),
        "slope": random.randint(0, 2),
        "ca": random.randint(0, 4),
        "thal": random.randint(0, 3)
    }


def main():
    print(" Request generator started")
    print(f"➡️ Sending requests to: {PREDICTION_ENDPOINT}")

    while True:
        try:
            payload = generate_payload()
            response = requests.post(PREDICTION_ENDPOINT, json=payload)

            print(
                f"Status: {response.status_code} | "
                f"Response: {response.json()}"
            )

        except Exception as e:
            print(f" Error: {e}")

        # Случайная задержка от 0 до 5 секунд
        time.sleep(random.uniform(0, 5))


if __name__ == "__main__":
    main()
