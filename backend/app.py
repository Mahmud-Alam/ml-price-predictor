from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return 'ML model is running!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    area = data.get('area')
    if area is None:
        return jsonify({'error': 'Missing area'}), 400

    prediction = model.predict([[area]])
    return jsonify({'predicted_price': round(max(0, prediction[0]), 2)})

if __name__ == '__main__':
    # app.run(port=5000, debug=True)
    # Use the PORT Render provides, default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
