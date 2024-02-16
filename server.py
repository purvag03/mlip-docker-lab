from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('iris_model.pkl')

@app.route('/predict', methods=['GET'])
def predict():
    # Get the input array from the request
    get_json = request.get_json()
    iris_input = get_json['input']
    
    # Convert input to 2D array
    iris_input_array = np.array(iris_input).reshape(1, -1)
    
    # Make prediction using the model
    prediction = model.predict(iris_input_array)
    
    # Return the prediction as a response
    return jsonify({'prediction': prediction.tolist()})

@app.route('/')
def hello():
    return 'Welcome to Docker Lab'

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
