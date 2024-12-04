from flask import Blueprint, jsonify, request
from src.models.health_model import predict_health_risk
from src.utils.data_preprocessing import preprocess_data

bp = Blueprint('api', __name__)

@bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    processed_data = preprocess_data(data)
    prediction = predict_health_risk(processed_data)
    return jsonify({"prediction": prediction})
