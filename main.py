from flask import Flask, request, jsonify
import tensorflow as tf
import predictloker

app = Flask(__name__)
app.debug = True


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
        prediction = predictionloker.predict_loker(keterampilan, peminatan)

        output = {
            "result": prediction
        }

        return jsonify(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
