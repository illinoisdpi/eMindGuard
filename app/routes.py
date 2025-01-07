from flask import Flask, Blueprint, render_template, request, jsonify
import numpy as np
import pickle
import dill
import torch
import numpy as np




main = Blueprint('main', __name__)

# Load model and scaler
model_path = "models/mental_health_predictor.pkl"

scaler_path = "models/scaler.pkl"

with open(model_path, "rb") as f:
    model = dill.load(f)


with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/predict", methods=["POST"])
def predict():
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Extract and validate values
        socioEconomic = float(data.get('socioEconomic', 0) / 100)
        household = float(data.get('household', 0) / 100 )
        behavioral = float(data.get('behavioral', 0) / 100)
        chronic = float(data.get('chronic', 0) / 100)
        wellBeing = float(data.get('wellBeing', 0) / 100)

        # Prepare input for the model
        input_features = np.array([[socioEconomic, household, behavioral, chronic, wellBeing]])
        input_features = scaler.transform(input_features)  # Apply the saved scaler

        # Predict the mental health score
        model.eval()
        predicted_score = model(torch.tensor(input_features, dtype=torch.float32)).item()
        print(predicted_score)

        return jsonify({'score': float(predicted_score)})
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': 'Invalid input or server error'}), 400