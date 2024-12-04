from flask import Flask, jsonify, request
from src.models.health_model import predict_health_risk
from src.utils.data_preprocessing import preprocess_data

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    processed_data = preprocess_data(data)
    prediction = predict_health_risk(processed_data)
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True)
