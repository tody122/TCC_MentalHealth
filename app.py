from flask import Flask, request, jsonify
import joblib
import numpy as np
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Carregue o pipeline treinado
pipeline = joblib.load('pipeline_mlp.pkl')
THRESHOLD = 0.4

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        dados = request.json
        logger.info(f'Dados recebidos: {dados}')
        
        # Converter valores string para float
        dados_convertidos = {k: float(v) if v != 'null' else 0.0 for k, v in dados.items()}
        logger.info(f'Dados convertidos: {dados_convertidos}')
        
        # Garantir ordem correta das features
        features = ['MH6', 'Subjective_Income', 'MH7B2', 'Household_Income', 'W3', 'WP21759']
        entrada = np.array([[dados_convertidos[f] for f in features]])
        logger.info(f'Array de entrada: {entrada}')
        
        proba = pipeline.predict_proba(entrada)[:, 1][0]
        previsao = int(proba >= THRESHOLD)
        
        resposta = {
            "previsao": previsao,
            "probabilidade_doente": float(proba),
            "threshold_utilizado": THRESHOLD
        }
        logger.info(f'Resposta: {resposta}')
        
        return jsonify(resposta)
    except Exception as e:
        logger.error(f'Erro ao processar requisição: {str(e)}')
        return jsonify({"erro": str(e)}), 500

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
