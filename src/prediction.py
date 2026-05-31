import joblib
import numpy as np

# Load model and scaler
model = joblib.load("model/crop_model.pkl")
scaler = joblib.load("model/scaler.pkl")

def predict_crop(N, P, K, temperature, humidity, ph, rainfall):

    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    # Scale input
    scaled_features = scaler.transform(features)

    # Predict
    prediction = model.predict(scaled_features)

    return prediction[0]