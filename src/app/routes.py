from flask import Blueprint, jsonify, request
from ..models.health_model import predict_health_risk
from ..utils.data_preprocessing import preprocess_data

bp = Blueprint('api', __name__)

@bp.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse incoming JSON
        data = request.get_json()

        # Preprocess data
        processed_data = preprocess_data(data)

        # Make prediction
        prediction = predict_health_risk(processed_data)

        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
