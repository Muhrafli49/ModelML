from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model('linear.h5')


@app.route('/', methods=['GET'])
def home():
    return "API is running!"


@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json()

    # Perform data preprocessing if needed
    data_predict = int(data["data"])

    # Make predictions using the loaded model
    predictions = model.predict([[data_predict]])

    # Perform data postprocessing if needed
    # ...

    # Return the predictions as a JSON response
    return jsonify(predictions.item())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
