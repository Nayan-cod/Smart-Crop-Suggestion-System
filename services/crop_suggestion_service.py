import pickle
import numpy as np

MODEL_PATH = "model.pkl"

def load_model():
    return pickle.load(open(MODEL_PATH, 'rb'))

def suggest_crop(N: float, P: float, K: float, temp: float, humidity: float, ph: float, rainfall: float) -> str:
    model = load_model()
    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)
    prediction = model.predict(single_pred)
    return prediction.item().title()
