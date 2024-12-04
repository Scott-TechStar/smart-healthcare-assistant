from sklearn.metrics import accuracy_score, confusion_matrix

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    cm = confusion_matrix(y_test, predictions)
    
    print(f"Accuracy: {accuracy}")
    print(f"Confusion Matrix: \n{cm}")
    return accuracy, cm
