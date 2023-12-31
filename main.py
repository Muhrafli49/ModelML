from flask import Flask, request, jsonify
import tensorflow as tf
import predictloker


app = Flask(__name__)


# Load model
model = tf.keras.models.load_model('linear.h5')


@app.route('/', methods=['GET'])
def home():
    return "API is running!"


@app.post("/predict")
def predict_text():
    try:
        req = request.get_json()  # Mendapatkan data JSON dari permintaan
        keterampilan = req.get('keterampilan')
        peminatan = req.get('peminatan')

        predict = predictloker.predict_loker(keterampilan, peminatan)

        output = {
            "result": predict
        }

        return jsonify(output)
    except Exception as e:
        return "Internal Server Error", 500

        return "Internal Server Error"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
