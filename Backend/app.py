# app.py
import joblib
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

# Inicializa a API Flask
app = Flask(__name__)
CORS(app)

# Carrega os modelos
modelo_rf = joblib.load("modelo_rf.pkl")
modelo_mlp = joblib.load("modelo_mlp.pkl")
modelo_gb = joblib.load("modelo_gb.pkl")

# Carrega scaler, PCA e features
scaler = joblib.load("scaler.pkl")
pca = joblib.load("pca.pkl")
features = joblib.load("features.pkl")  # lista com strings dos nomes das features

@app.route('/')
def index():
    return "API de Saúde Mental funcionando!"

@app.route('/prever', methods=['POST'])
def prever():
    try:
        dados = request.get_json()
        entrada = np.array([[dados[feat] for feat in features]])
        entrada = scaler.transform(entrada)
        entrada = pca.transform(entrada)

        resultado = {
            "RandomForest": int(modelo_rf.predict(entrada)[0]),
            "MLP": int(modelo_mlp.predict(entrada)[0]),
            "GradientBoosting": int(modelo_gb.predict(entrada)[0])
        }

        return jsonify(resultado)

    except Exception as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=False)