from flask import Flask, request, jsonify
import joblib
import numpy as np

# Carregue o pipeline treinado
pipeline = joblib.load('pipeline_mlp.pkl')
THRESHOLD = 0.4

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    dados = request.json  # Exemplo: {"idade": 25, "sexo": 1, ...}
    entrada = np.array([list(dados.values())])  # Garanta ordem correta das features!
    proba = pipeline.predict_proba(entrada)[:, 1][0]
    previsao = int(proba >= THRESHOLD)
    return jsonify({
        "previsao": previsao,
        "probabilidade_doente": float(proba),
        "threshold_utilizado": THRESHOLD
    })

if __name__ == '__main__':
    app.run(debug=True)
