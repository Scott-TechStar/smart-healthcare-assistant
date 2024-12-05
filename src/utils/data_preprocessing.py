import os
import pandas as pd

def preprocess_data(input_data):
    """
    Preprocess input data (JSON or dictionary) and combine with CSV data.
    """
    # Get the directory of this script
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct absolute paths for the CSV files
    symptoms_file = os.path.join(base_dir, '../../data/sample_data/symptoms_data.csv')
    patient_file = os.path.join(base_dir, '../../data/sample_data/patient_data.csv')

    # Load CSVs
    symptoms_df = pd.read_csv(symptoms_file).applymap(lambda x: 1 if x == 'yes' else 0)
    patient_df = pd.read_csv(patient_file)
    patient_df['smoker'] = patient_df['smoker'].map({'yes': 1, 'no': 0})
    patient_df['exercise_level'] = patient_df['exercise_level'].map({'low': 0, 'medium': 1, 'high': 2})

    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])

    # Map 'yes'/'no' in input to numeric values
    for symptom in ['fever', 'cough', 'headache', 'chest_pain']:
        if symptom in input_df:
            input_df[symptom] = input_df[symptom].map({'yes': 1, 'no': 0})

    # Calculate BMI if not provided
    if "BMI" not in input_df:
        input_df["BMI"] = input_df["weight"] / (input_df["height"] / 100) ** 2

    # Return processed data
    return input_df
