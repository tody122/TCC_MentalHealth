import requests
import json

# Dados de teste baseados no dataset real
dados = {
    "W1": 3.0,
    "W2": 4.0,
    "W3": 0.0,
    "W4": 2.0,
    "W5A": 3.0,
    "W5B": 1.0,
    "W5C": 3.0,
    "W5D": 1.0,
    "W5E": 4.0,
    "W5F": 1.0,
    "W5G": 3.0,
    "W6": 4.0,
    "W7A": 4.0,
    "W7B": 3.0,
    "W7C": 1.0,
    "W8": 1.0,
    "W9": 2.0,
    "W11A": 4.0,
    "W11B": 4.0,
    "MH1": 3.0,
    "MH2A": 4.0,
    "MH2B": 4.0,
    "MH3A": 4.0,
    "MH3B": 1.0,
    "MH3C": 4.0,
    "MH3D": 4.0,
    "MH4A": 4.0,
    "MH4B": 1.0,
    "MH5": 2.0,
    "MH6": 2.0,
    "MH7A": 1.0,
    "W27": 1.0,
    "W28": 6.0,
    "W29": 4.0,
    "age_var3": 4.0,
    "Gender": 1.0,
    "Education": 3.0,
    "Household_Income": 3.0,
    "wbi": 3.0,
    "Subjective_Income": 2.0,
    "COUNTRYNEW_Argentina": 0.0,
    "COUNTRYNEW_Bolivia": 0.0,
    "COUNTRYNEW_Brazil": 0.0,
    "COUNTRYNEW_Chile": 0.0,
    "COUNTRYNEW_Colombia": 0.0,
    "COUNTRYNEW_Ecuador": 0.0,
    "COUNTRYNEW_Paraguay": 0.0,
    "COUNTRYNEW_Peru": 0.0,
    "COUNTRYNEW_Uruguay": 0.0,
    "COUNTRYNEW_Venezuela": 1.0,
    "MH7B_2_": 1.0,
    "MH7B_2_1": 0.0,
    "MH7B_2_2": 0.0,
    "MH7B_2_3": 0.0,
    "MH7B_2_4": 0.0,
    "MH7B_2_5": 0.0,
    "MH7B_2_99": 0.0,
    "EMP_2010_1": 0.0,
    "EMP_2010_2": 0.0,
    "EMP_2010_3": 0.0,
    "EMP_2010_4": 0.0,
    "EMP_2010_5": 0.0,
    "EMP_2010_6": 1.0
}

# Testando a rota principal
print("Testando a rota principal...")
response = requests.get("http://localhost:5000/")
print("Resposta da rota principal:", response.text)

# Testando a rota de previsão
print("\nTestando a rota de previsão...")
response = requests.post(
    "http://localhost:5000/prever",
    json=dados,
    headers={"Content-Type": "application/json"}
)
print("Status code:", response.status_code)
print("Resposta da rota de previsão:", response.text) 