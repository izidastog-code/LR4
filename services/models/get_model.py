import os
import pickle

def main():
    # Путь к исходному файлу модели в mlflow artifacts
    source_path = "/home/user/my_proj/mlflow/mlartifacts/1/3dd1099eae3040e286f0006a0666caa2/artifacts/model/model.pkl"
    print("Loading PICKLE model from:", source_path)

    with open(source_path, "rb") as f:
        model = pickle.load(f)

    # Путь, куда сохранить модель для сервиса
    target_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    print("Saving model to:", target_path)

    with open(target_path, "wb") as f:
        pickle.dump(model, f)

    print("Model saved successfully!")


if __name__ == "__main__":
    main()
