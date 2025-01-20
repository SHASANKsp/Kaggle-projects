from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

with open("Plant_health_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class ModelInput(BaseModel):
    Soil_Moisture: float
    Nitrogen_Level: float


@app.post("/predict")
def predict(input_data: ModelInput):
    features = np.array([[input_data.Soil_Moisture, input_data.Nitrogen_Level]])
    prediction = model.predict(features)
    if prediction == 0: 
        prediction = "Healthy"
    elif prediction == 1: 
        prediction = "High Stress"
    elif prediction == 2: 
        prediction = "Moderate Stress"
    return {"prediction": prediction}
