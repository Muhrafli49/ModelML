from flask import Flask, request, jsonify
import tensorflow as tf
import traceback

app = Flask(__name__)
app.debug = True

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

        # Lakukan prediksi menggunakan model
        prediction = model.predict([[keterampilan, peminatan]])

        output = {
            "result": prediction.tolist()
        }

        return jsonify(output)
    except Exception as e:
        traceback.print_exc()
        return "Internal Server Error", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
