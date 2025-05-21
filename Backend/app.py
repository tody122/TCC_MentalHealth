from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

app = Flask(__name__)
CORS(app)  # Permite requisições de diferentes origens

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "API da IA está funcionando!"
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # Aqui você vai adicionar o código para carregar seu modelo
        # e fazer as previsões
        
        # Exemplo de resposta:
        return jsonify({
            "status": "success",
            "prediction": "resultado da sua IA aqui"
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 