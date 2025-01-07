from app.models import MentalHealthPredictor
import pickle

with open("../models/mental_health_predictor.pkl", "rb") as f:
    model = pickle.load(f)
    print("Model loaded successfully!")