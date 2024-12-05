def health_suggestions(prediction):
    if prediction == "High Risk":
        return "Consider seeing a doctor immediately and review your lifestyle habits."
    elif prediction == "Medium Risk":
        return "Maintain a healthy lifestyle with balanced nutrition and regular checkups."
    else:
        return "Keep up the good work! Maintain a healthy diet and exercise regularly."
