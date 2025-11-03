# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import torch
import torch.nn.functional as F # Importe se seu 'forward' usar

# Importa a classe da sua rede do outro arquivo
from model_definition import Model 

# --- 1. Inicialização da API ---
app = FastAPI()

# --- 2. Carregamento do Modelo ---
# O modelo é carregado UMA VEZ quando a API inicia.
print("Carregando o modelo...")
model = Model() # Instancia a arquitetura

# Carrega os pesos (state_dict) que você treinou
# IMPORTANTE: map_location="cpu" força o modelo a rodar em CPU no Render
model.load_state_dict(torch.load("ModeloPytorchBalanceado.pt", map_location=torch.device('cpu')))

# IMPORTANTE: Coloca o modelo em modo de avaliação (desliga dropout, etc.)
model.eval() 
print("Modelo carregado com sucesso!")

# --- 3. Definição dos dados de entrada ---
# Define como o FastAPI deve esperar os dados (JSON)
# Exemplo: esperando uma lista de floats
class InputData(BaseModel):
    data: list[float] 

# --- 4. Criação do Endpoint de Previsão ---
@app.post("/predict")
async def predict(input_data: InputData):
    
    # --- 5. Pré-processamento ---
    # Converta a lista de dados recebida em um tensor
    # Esta é a parte mais CRÍTICA: o tensor DEVE ter o formato
    # exato que seu modelo espera (shape, tipo, normalização, etc.)
    
    # TODO: Ajuste esta linha para o seu modelo!
    # Exemplo para uma entrada de 784 features (imagem 28x28 achatada)
    try:
        # Converte a lista (ex: [0.1, 0.2, ...]) em tensor
        tensor_dados = torch.tensor(input_data.data).float() 
        
        # Ajusta o 'shape' (ex: de [784] para [1, 784])
        # O '1' no início é o 'batch size' (lote de 1)
        tensor_dados = tensor_dados.view(1, -1) 
        
    except Exception as e:
        # Retorna um erro se os dados de entrada estiverem errados
        return {"error": f"Erro no pré-processamento: {str(e)}"}

    # --- 6. Fazer a Previsão ---
    # 'with torch.no_grad():' é uma otimização que desliga
    # o cálculo de gradientes, economizando memória e CPU.
    with torch.no_grad():
        output = model(tensor_dados)
        
        # --- 7. Pós-processamento ---
        # Converte a saída do modelo (logits) em uma resposta final
        
        # Exemplo para classificação:
        # Aplica Softmax para obter probabilidades
        probabilidades = F.softmax(output, dim=1) 
        # Pega o índice (a classe) com a maior probabilidade
        _, predicted_idx = torch.max(probabilidades, 1)
        
        prediction = predicted_idx.item() # Converte de tensor para número (ex: 7)
        confidence = probabilidades.max().item() # Pega a confiança (ex: 0.95)

    # --- 8. Retornar a Resposta (JSON) ---
    return {
        "predicted_class": prediction,
        "confidence": confidence
    }

# Endpoint "raiz" para verificar se a API está funcionando
@app.get("/")
def read_root():
    return {"status": "API do Modelo de ML está online!"}