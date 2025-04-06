from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

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
    return jsonify({'predicted_price': round(prediction[0], 2)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
