import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Example model training and prediction function
def train_model(data, labels):
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    print(f'Model Accuracy: {model.score(X_test, y_test)}')
    return model

def predict_health_risk(model, data):
    prediction = model.predict([data])
    return prediction[0]
