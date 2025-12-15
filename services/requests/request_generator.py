import time
import random
import requests

URL = "http://ml_service:8000/api/prediction"

payload = {
    "age": 55,
    "sex": 1,
    "cp": 2,
    "trestbps": 130,
    "chol": 250,
    "fbs": 0,
    "restecg": 1,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 1.2,
    "slope": 2,
    "ca": 0,
    "thal": 2
}

print("🚀 Request generator started")

while True:
    try:
        item_id = random.randint(1, 10_000)
        r = requests.post(
            URL,
            params={"item_id": item_id},
            json=payload,
            timeout=3
        )
        print(f"✅ {item_id} → {r.status_code} → {r.json()}")
    except Exception as e:
        print(f"❌ Error: {e}")

    time.sleep(random.uniform(0, 5))
