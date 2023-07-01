import traceback

import utils
from ai import StableDiffusion

from flask import Flask, jsonify, Response

# Create server
app = Flask(__name__)

# Create model
model = StableDiffusion()

@app.route("/")
def index():
    msg = '''Para poder solicitar una prediccion debe acceder al endpoint:
            /predict/<input_text>
            Debe reemplazar <input_text> en el explorador por el texto
            que desea ingresar al modelo
            '''
    return msg

@app.route("/api/v1.0/predict/", methods=['POST'])
def api_predict():
    return {"inference": "hola"}


@app.route("/predict/<input_text>/render", methods=['POST'])
def predict(input_text):
    try:
        # Predict
        img_data = model.predict(input_text)
        image_html = utils.graph(img_data[0])
        return Response(image_html.getvalue(), mimetype='image/png')
    except:
        # Error
        return jsonify({'trace': traceback.format_exc()})


with app.app_context():
    # Build model (download and set weights)
    model.build_model()
    print("Base de datos generada")


if __name__ == '__main__':
    # Server start
    app.run(host="127.0.0.1", port=5000, debug=True)