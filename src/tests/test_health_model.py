import pytest
from src.models.health_model import train_model, predict_health_risk

def test_train_model():
    # Mock data for testing
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    labels = [0, 1, 0]
    
    model = train_model(data, labels)
    
    assert model is not None
    assert hasattr(model, 'predict')

def test_predict_health_risk():
    # Mock trained model and input data
    model = train_model([[1, 2, 3], [4, 5, 6]], [0, 1])
    prediction = predict_health_risk(model, [1, 2, 3])
    
    assert prediction in [0, 1]  # Assuming binary classification (e.g., risk/no-risk)
