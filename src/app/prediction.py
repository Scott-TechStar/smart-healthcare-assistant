import pandas as pd

def predict_health_risk(input_data):
    """
    This function predicts health risk based on a combination of symptoms and patient data.
    """
    age = input_data["age"]
    BMI = input_data["BMI"]
    fever = input_data["fever"]
    cough = input_data["cough"]
    headache = input_data["headache"]
    chest_pain = input_data["chest_pain"]

    # Simple rule-based prediction
    if age > 50 and fever and chest_pain and headache:
        return "High Risk"
    elif BMI > 30 or (fever and cough):
        return "Medium Risk"
    elif BMI == 20 and age > 15 and not fever and not chest_pain and not headache:
        return "Weight Issues"
    else:
        return "Low Risk"
