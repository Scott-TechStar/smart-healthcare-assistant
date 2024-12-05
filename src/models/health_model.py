import pandas as pd

def predict_health_risk(data):
    """
    Predict health risk based on symptoms and patient data.
    """
    # Extract features
    age = data["age"].iloc[0] if "age" in data else 0
    BMI = data["BMI"].iloc[0] if "BMI" in data else 0
    fever = data["fever"].iloc[0] if "fever" in data else 0
    cough = data["cough"].iloc[0] if "cough" in data else 0
    headache = data["headache"].iloc[0] if "headache" in data else 0
    chest_pain = data["chest_pain"].iloc[0] if "chest_pain" in data else 0

    # Simple rule-based prediction
    if age > 50 and fever == 1 and chest_pain == 1 and headache == 1:
        return "High Risk"
    elif BMI > 30 or (fever == 1 and cough == 1):
        return "Medium Risk"
    elif BMI == 20 and age > 15 and fever == 0 and chest_pain == 0 and headache == 0:
        return "Weight Issues"
    else:
        return "Low Risk"
