from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the pre-trained CNN-LSTM model
MODEL_PATH = "models/cnn_lstm_model.pkl"
# with open(MODEL_PATH, "rb") as model_file:
#     model = pickle.load(model_file)



UPLOAD_FOLDER = "uploads/eeg_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


import random

def dummy_predict(data):
    # Generate a random number between 0 and 9
    return [random.randint(0, 9)]

model = {"predict": dummy_predict}


# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'eeg_file' not in request.files:
#         return jsonify({"error": "No file uploaded"}), 400

#     eeg_file = request.files['eeg_file']
#     file_path = os.path.join(UPLOAD_FOLDER, eeg_file.filename)
#     eeg_file.save(file_path)

#     try:
#         # Load and preprocess EEG data
#         eeg_data = np.loadtxt(file_path, delimiter=",")  # Example format
#         eeg_data = preprocess_eeg(eeg_data)

#         # Make prediction using the model
#         prediction = model.predict([eeg_data])
#         predicted_text = decode_prediction(prediction)

#         return jsonify({"text": predicted_text})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

@app.route('/predict', methods=['POST'])
def predict():
    if 'eeg_file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    eeg_file = request.files['eeg_file']
    file_path = os.path.join(UPLOAD_FOLDER, eeg_file.filename)
    eeg_file.save(file_path)

    try:
        # Dummy prediction
        random_number = random.randint(0, 9)
        print(f"Generated random number: {random_number}")
        return jsonify({"text": str(random_number)})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


def preprocess_eeg(data):
    """
    Preprocess EEG data to match the input shape expected by the model.
    """
    # Example preprocessing: Normalize data and reshape
    data = (data - np.mean(data)) / np.std(data)
    return data.reshape(1, -1, data.shape[1])  # Adjust dimensions for your model

# def decode_prediction(prediction):
#     """
#     Decode the model's output into text.
#     """
#     # Example: Map prediction indices to characters
#     alphabet = "0123456789"
#     return "".join([alphabet[i] for i in prediction])

def decode_prediction(prediction):
    """
    Decode the model's output into text.
    """
    return str(prediction[0])  # Return the random number as a string


if __name__ == '__main__':
    app.run(debug=True, port=5000)
