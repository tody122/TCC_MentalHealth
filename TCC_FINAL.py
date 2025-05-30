# -*- coding: utf-8 -*-
"""Cópia de TCC_FINAL.ipynb

Automatically generated by Colab.

Original file is located at
    https://tcc-mentalhealth.onrender.com
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
from sklearn.preprocessing import LabelEncoder, StandardScaler, OrdinalEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import random
from pprint import pprint
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from sklearn.decomposition import PCA
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import GradientBoostingClassifier

# ====== TREINAMENTO DOS MODELOS ======
print("Iniciando treinamento dos modelos...")

# Importando o dataset
df = pd.read_csv("Mentalhealth.csv", low_memory=False)

# Filtrando para países sul-americanos
paises_sul_americanos = [
    'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia',
    'Ecuador', 'Paraguay', 'Peru', 'Uruguay', 'Venezuela'
]
df_SulAmericanos = df[df['COUNTRYNEW'].isin(paises_sul_americanos)]

# Removendo colunas desnecessárias
df_SulAmerica_util = df_SulAmericanos.drop(columns=['WPID_RANDOM', 'FIELD_DATE', 'PROJWT', 'WGT',
                      'YEAR_WAVE','Global11Regions','age_var1',
                      'age_var2', 'Age','WP21757', 'WP21758',
                      'WP21759', 'WP21760', 'WP21761', 'WP21768',
                      'W10', 'W13', 'W14', 'W15',
                      'W15_1A', 'W15_1B', 'W15_1C',
                      'W15_1D','W15_1E','W15_2A', 'W15_2B','W30'])

# Transformando colunas
colunas_ordinais = [
    'W1','W2','W3', 'W4', 'W5A','W5B','W5C', 'W5D','W5E','W5F','W5G','W6','W7A','W7B', 'W7C','W8','W9','W11A',
    'W14','W11B', 'W30', 'age_mh', 'Household_Income',
    'MH1', 'MH2A', 'MH2B', 'MH3B', 'MH4B', 'MH5', 'MH6', 'MH3A','MH3B','MH3C','MH3D',
    'MH4A','MH4B','MH5','MH9A','MH9B', 'MH9C', 'MH9D', 'MH9E', 'MH9F',
    'MH9G','MH9H','W28','W29', 'age_mh', 'wbi', 'subjective_Income'
]

colunas_nominais = ['COUNTRYNEW','MH7B_2','EMP_2010']
colunas_booleanas = ['MH6','MH7A','MH7C','MH8A','MH8B','MH8C','MH8D','MH8E','MH8F','MH8G','MH8H','W27']

# Processando colunas ordinais
for col in colunas_ordinais:
    if col in df_SulAmerica_util.columns:
        df_SulAmerica_util[col] = df_SulAmerica_util[col].replace([' ', '', '99', 99], np.nan)
        df_SulAmerica_util[col] = pd.to_numeric(df_SulAmerica_util[col], errors='coerce')

# Processando colunas booleanas
for col in colunas_booleanas:
    if col in df_SulAmerica_util.columns:
        df_SulAmerica_util[col] = df_SulAmerica_util[col].astype(str).str.strip()
        df_SulAmerica_util[col] = df_SulAmerica_util[col].replace({
            '1': 1, '2': 0, '99': np.nan, '99.0': np.nan, '': np.nan, 'nan': np.nan
        })
        df_SulAmerica_util[col] = pd.to_numeric(df_SulAmerica_util[col], errors='coerce')
        df_SulAmerica_util[col] = df_SulAmerica_util[col].astype('Int64')

# Criando variáveis dummy
df_Numerico = pd.get_dummies(df_SulAmerica_util, columns=colunas_nominais, dummy_na=False)

# Removendo colunas com muitos valores nulos
df_Numerico_Relevantes = df_Numerico.drop(columns=['MH9D','MH9A','MH9B', 'MH9F', 'MH8G', 'age_mh',
                                        'MH8H', 'MH8E', 'MH7C','MH8B','MH8C', 'MH8D',
                                        'MH8A', 'MH9G','MH9G', 'MH9E', 'MH9C', 'MH7B', 'MH8F', 'MH9H'])

# Tratando valores nulos
for col in df_Numerico_Relevantes.columns:
    if df_Numerico_Relevantes[col].isnull().sum() > 0:
        media = df_Numerico_Relevantes[col].mean()
        media_arredondada = round(media)
        df_Numerico_Relevantes[col] = df_Numerico_Relevantes[col].fillna(media_arredondada)

# Preparando dados para treinamento
X = df_Numerico_Relevantes.drop('MH7A', axis=1)
y = df_Numerico_Relevantes['MH7A']

# Aplicando PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=5, random_state=42)
X_pca = pca.fit_transform(X_scaled)

# Dividindo dados
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42, stratify=y)

# Balanceando dados
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Treinando modelos
print("Treinando Random Forest...")
modelo_rf = RandomForestClassifier(random_state=42)
modelo_rf.fit(X_train_res, y_train_res)

print("Treinando MLP...")
modelo_mlp = MLPClassifier(random_state=42, max_iter=300)
modelo_mlp.fit(X_train_res, y_train_res)

print("Treinando Gradient Boosting...")
modelo_gb = GradientBoostingClassifier(random_state=42)
modelo_gb.fit(X_train_res, y_train_res)

# Salvando modelos e objetos
print("Salvando modelos e objetos...")
joblib.dump(modelo_rf, 'modelo_rf.pkl')
joblib.dump(modelo_mlp, 'modelo_mlp.pkl')
joblib.dump(modelo_gb, 'modelo_gb.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(pca, 'pca.pkl')
joblib.dump(X.columns.tolist(), 'features.pkl')
print('Modelos e objetos salvos com sucesso!')

# ====== CONFIGURAÇÃO DO SERVIDOR FLASK ======
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "API de Saúde Mental está funcionando!"

@app.route('/prever', methods=['POST'])
def prever():
    try:
        dados = request.get_json()
        if not dados:
            return jsonify({'erro': 'Nenhum dado recebido'}), 400

        df_input = pd.DataFrame([dados])

        # Selecionar e reordenar as features necessárias
        df_input = df_input[X.columns.tolist()]

        # Pré-processar
        dados_escalados = scaler.transform(df_input)
        dados_pca = pca.transform(dados_escalados)

        # Previsões
        pred_rf = modelo_rf.predict(dados_pca)[0]
        pred_mlp = modelo_mlp.predict(dados_pca)[0]
        pred_gb = modelo_gb.predict(dados_pca)[0]

        # Retornar resultados
        return jsonify({
            'RandomForest': int(pred_rf),
            'MLP': int(pred_mlp),
            'GradientBoosting': int(pred_gb)
        })

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

"""#IMPORTANDO O DATASET"""

df = pd.read_csv("Mentalhealth.csv", low_memory=False)

df.head()

"""#ANALISE EXPLORATORIA DE DADOS E PRÉ-PROCESSAMENTO

##Filtrando o dataset para somente paises sul americanos
"""

# Verificar o nome exato da coluna de países
df['COUNTRYNEW'].unique()

paises_sul_americanos = [
    'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia',
    'Ecuador', 'Paraguay', 'Peru', 'Uruguay', 'Venezuela'
]

df_SulAmericanos = df[df['COUNTRYNEW'].isin(paises_sul_americanos)]

#Verificando a quantidade de amostras do novo dataset
df_SulAmericanos['COUNTRYNEW'].unique()

"""##Removendo colunas que sao somente de descrição ou não tem necessidade de estudo para o dataset"""

df_SulAmerica_util = df_SulAmericanos.drop(columns=['WPID_RANDOM', 'FIELD_DATE', 'PROJWT', 'WGT',
                      'YEAR_WAVE','Global11Regions','age_var1',
                      'age_var2', 'Age','WP21757', 'WP21758',
                      'WP21759', 'WP21760', 'WP21761', 'WP21768',
                      'W10', 'W13', 'W14', 'W15',
                      'W15_1A', 'W15_1B', 'W15_1C',
                      'W15_1D','W15_1E','W15_2A', 'W15_2B','W30'])
df_SulAmerica_util.info()

"""## Transformando as colunas object em int e aplicando ordinalidade ( se necessario )"""

colunas_ordinais = [
    'W1','W2','W3', 'W4', 'W5A','W5B','W5C', 'W5D','W5E','W5F','W5G','W6','W7A','W7B', 'W7C','W8','W9','W11A'
    ,'W14','W11B',
    'W30', 'age_mh', 'Household_Income',
    'MH1', 'MH2A', 'MH2B', 'MH3B', 'MH4B', 'MH5', 'MH6', 'MH3A','MH3B','MH3C','MH3D',
    'MH4A','MH4B','MH5','MH9A','MH9B', 'MH9C', 'MH9D', 'MH9E', 'MH9F',
    'MH9G','MH9H','W28','W29', 'age_mh', 'wbi', 'subjective_Income'
]

colunas_ordinais_inverter = [
    'W1','W2','W3', 'W4', 'W5A','W5B','W5C', 'W5D','W5E','W5F','W5G','W6','W7A','W7B', 'W7C','W8','W9','W11A'
    ,'W14','W11B',
    'W30',
    'MH1', 'MH2A', 'MH2B', 'MH3B', 'MH4B', 'MH5', 'MH6', 'MH3A','MH3B','MH3C','MH3D',
    'MH4A','MH4B','MH5','MH9A','MH9B', 'MH9C', 'MH9D', 'MH9E', 'MH9F',
    'MH9G','MH9H','W28','W29', 'age_mh', 'wbi', 'subjective_Income'
]

colunas_nominais = ['COUNTRYNEW','MH7B_2','EMP_2010']

colunas_booleanas = ['MH6','MH7A','MH7C','MH8A','MH8B','MH8C','MH8D','MH8E','MH8F','MH8G','MH8H','W27']

for col in colunas_ordinais:
    if col in df_SulAmerica_util.columns:
        df_SulAmerica_util[col] = df_SulAmerica_util[col].replace([' ', '', '99', 99], np.nan)
        df_SulAmerica_util[col] = pd.to_numeric(df_SulAmerica_util[col], errors='coerce')


for col in colunas_booleanas:
    if col in df_SulAmerica_util.columns:
        df_SulAmerica_util[col] = df_SulAmerica_util[col].astype(str).str.strip()
        df_SulAmerica_util[col] = df_SulAmerica_util[col].replace({
            '1': 1, '2': 0, '99': np.nan, '99.0': np.nan, '': np.nan, 'nan': np.nan
        })
        df_SulAmerica_util[col] = pd.to_numeric(df_SulAmerica_util[col], errors='coerce')
        df_SulAmerica_util[col] = df_SulAmerica_util[col].astype('Int64')


df_Numerico = pd.get_dummies(df_SulAmerica_util, columns=colunas_nominais, dummy_na=False)

colunas_Onehot = df_Numerico.select_dtypes(include='bool').columns

df_Numerico[colunas_Onehot] = df_Numerico[colunas_Onehot].astype('float')

df_Numerico['MH7B'] = df_Numerico['MH7B'].astype(str).str.strip()

df_Numerico['MH7B'] = df_Numerico['MH7B'].replace({
    '99': np.nan,
    '97+': np.nan,
    '97': np.nan,
    '': np.nan,
    'nan': np.nan
})

df_Numerico['MH7B'] = pd.to_numeric(df_Numerico['MH7B'], errors='coerce')

df_Numerico['MH7B'] = df_Numerico['MH7B'].astype('Int64')



for col in colunas_ordinais_inverter:
    if col in df_Numerico.columns:
        valores = df_Numerico[col].dropna().unique()
        if len(valores) > 1:
            max_val = max(valores)
            min_val = min(valores)
            df_Numerico[col] = df_Numerico[col].apply(
                lambda x: (max_val + min_val) - x if pd.notna(x) else x
            )

df_Numerico.head()

"""##Verificando valores nulos"""

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df_Numerico.isnull().sum().sort_values(ascending=False)

"""##Excluindo colunas que possuem muitos valores nulos ou que são incongruentes com o projeto"""

#Colunas removidas pois são dados somente preenchidos caso a pessoa tenha dito possuir a doença, o que não faz sentido na hora da previsão (por conta disso o grande numero de NaN)
df_Numerico_Relevantes = df_Numerico.drop(columns=['MH9D','MH9A','MH9B', 'MH9F', 'MH8G', 'age_mh'
                                        , 'MH8H', 'MH8E', 'MH7C','MH8B','MH8C', 'MH8D',
                                        'MH8A', 'MH9G','MH9G', 'MH9E', 'MH9C', 'MH7B', 'MH8F', 'MH9H'])



df_Numerico_Relevantes = df_Numerico_Relevantes.apply(pd.to_numeric, errors='coerce').astype('float64')



df_Numerico_Relevantes.isnull().sum().sort_values(ascending=False)

"""##Tratando valores nulos"""

for col in df_Numerico_Relevantes.columns:
    if df_Numerico_Relevantes[col].isnull().sum() > 0:
        try:
            media = df_Numerico_Relevantes[col].mean()
            media_arredondada = round(media)
            df_Numerico_Relevantes[col] = df_Numerico_Relevantes[col].fillna(media_arredondada)
            print(f"{col}: preenchido com média arredondada -> {media_arredondada}")
        except TypeError:
            print(f"{col}: tipo não numérico ou erro ao calcular média")

df_Numerico_Relevantes.isnull().sum().sort_values(ascending=False)

print(df_Numerico_Relevantes.head())

"""#Teste

##KBest
"""

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


X_Kbest = df_Numerico_Relevantes.drop(columns=['MH7A'])
y = df_Numerico_Relevantes['MH7A']

X_train, X_test, y_train, y_test = train_test_split(X_Kbest, y, test_size=0.2, stratify=y, random_state=42)

from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

X_train_res = pd.DataFrame(X_train_res, columns=X_train.columns)


y_train_res.value_counts().plot.pie( autopct='%.2f')

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import mutual_info_classif


pipeline_rf = Pipeline([
    ('kbest', SelectKBest(k=12)),
    ('model', RandomForestClassifier(random_state=42))
])

pipeline_rf.fit(X_train, y_train)
y_pred_rf = pipeline_rf.predict(X_test)

print("=== RANDOM FOREST ===")
print("Acurácia:", accuracy_score(y_test, y_pred_rf))
print("Recall:", recall_score(y_test, y_pred_rf))

cm = confusion_matrix(y_test, y_pred_rf)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Matriz de Confusão - Random Forest")
plt.xlabel("Previsão")
plt.ylabel("Real")
plt.show()

from sklearn.neural_network import MLPClassifier

pipeline_mlp = Pipeline([
    ('kbest', SelectKBest(k=15)),
    ('model', MLPClassifier(random_state=42, max_iter=300))
])

pipeline_mlp.fit(X_train, y_train)
y_pred_mlp = pipeline_mlp.predict(X_test)

print("=== MLPClassifier ===")
print("Acurácia:", accuracy_score(y_test, y_pred_mlp))
print("Recall:", recall_score(y_test, y_pred_mlp))

cm = confusion_matrix(y_test, y_pred_mlp)
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens')
plt.title("Matriz de Confusão - MLP")
plt.xlabel("Previsão")
plt.ylabel("Real")
plt.show()

"""##Aplicando relação mutua"""

from sklearn.feature_selection import mutual_info_classif

# Define X e y a partir do seu DataFrame
X = df_Numerico_Relevantes.drop(columns=['MH7A'])
y = df_Numerico_Relevantes['MH7A']

mi_scores = mutual_info_classif(X, y, discrete_features='auto', random_state=42)

# Cria DataFrame com os resultados
mi_df = pd.DataFrame({
    'Feature': X.columns,
    'Mutual Information': mi_scores
})

# Ordena por relevância
mi_df_sorted = mi_df.sort_values(by='Mutual Information', ascending=False)

# Exibe o resultado
print(mi_df_sorted)

#Filtro baseado nas 8 melhores features

top_features = mi_df_sorted.head(8)['Feature'].tolist()

X_filtrado = X[top_features]

X_train, X_test, y_train, y_test = train_test_split(X_filtrado, y, test_size=0.2, random_state=42)

"""###Fazendo o Balanceamento"""

from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

X_train_res = pd.DataFrame(X_train_res, columns=X_train.columns)


y_train_res.value_counts().plot.pie( autopct='%.2f')

"""###Random forest"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix, classification_report

# Treinamento
modelo_rf = RandomForestClassifier(random_state=42)
modelo_rf.fit(X_train_res, y_train_res)

# Previsão
y_pred_rf = modelo_rf.predict(X_test)

# Avaliação
print("=== RANDOM FOREST ===")
print("Acurácia:", accuracy_score(y_test, y_pred_rf))
print("Recall:", recall_score(y_test, y_pred_rf))
print("\nMatriz de Confusão:")
# Gera a matriz de confusão
cm = confusion_matrix(y_test, y_pred_rf)  # ou y_pred_mlp, y_pred_gb dependendo do modelo
# Exibe visualmente
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Previsão')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()

"""###Redes neurais (MLPClassifier)"""

from sklearn.neural_network import MLPClassifier

# Treinamento
modelo_mlp = MLPClassifier(random_state=42, max_iter=300)
modelo_mlp.fit(X_train_res, y_train_res)

# Previsão
y_pred_mlp = modelo_mlp.predict(X_test)

# Avaliação
print("=== REDE NEURAL (MLP) ===")
print("Acurácia:", accuracy_score(y_test, y_pred_mlp))
print("Recall:", recall_score(y_test, y_pred_mlp))
print("\nMatriz de Confusão:")
# Gera a matriz de confusão
cm = confusion_matrix(y_test, y_pred_mlp)  # ou y_pred_mlp, y_pred_gb dependendo do modelo
# Exibe visualmente
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Previsão')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()

"""###Gradient Boosting"""

from sklearn.ensemble import GradientBoostingClassifier

# Treinamento
modelo_gb = GradientBoostingClassifier(random_state=42)
modelo_gb.fit(X_train_res, y_train_res)

# Previsão
y_pred_gb = modelo_gb.predict(X_test)

# Avaliação
print("=== GRADIENT BOOSTING ===")
print("Acurácia:", accuracy_score(y_test, y_pred_gb))
print("Recall:", recall_score(y_test, y_pred_gb))
print("\nMatriz de Confusão:")
cm = confusion_matrix(y_test, y_pred_gb)
sns.heatmap(cm, annot=True, fmt='d', cmap='Oranges', cbar=False)
plt.title("Matriz de Confusão - Gradient Boosting")
plt.xlabel("Previsão")
plt.ylabel("Real")
plt.show()

# ====== SALVANDO OS MODELOS E OBJETOS PARA A API ======
import joblib
joblib.dump(modelo_rf, 'modelo_rf.pkl')
joblib.dump(modelo_mlp, 'modelo_mlp.pkl')
joblib.dump(modelo_gb, 'modelo_gb.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(pca, 'pca.pkl')
joblib.dump(top_features, 'features.pkl')
print('Modelos e objetos salvos com sucesso!')

"""##Por filtro da correlação"""

#Correlação com a coluna alvo
correlacoes_com_alvo = df_Numerico_Relevantes.corr(numeric_only=True, method='kendall')['MH7A'].sort_values(key=abs, ascending=False)
print(correlacoes_com_alvo)

"""###Heatmap"""

correlacao = df_Numerico_Relevantes.corr(numeric_only=True, method='kendall')

# Definir o tamanho da figura com base no número de colunas
plt.figure(figsize=(len(correlacao.columns) * 0.6, len(correlacao.columns) * 0.6))

# Gerar o heatmap completo
sns.heatmap(
    correlacao,
    cmap='coolwarm',
    annot=True,
    fmt=".2f",
    linewidths=0.5,
    square=False,
    cbar_kws={"shrink": 0.5}
)

plt.title("Heatmap de Correlação Completo", fontsize=18)
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

#Filtro de limiar
limiar = 0.1
colunas_selecionadas = correlacoes_com_alvo[correlacoes_com_alvo.abs() >= limiar].index.tolist()

print(f"Colunas selecionadas correlação >= {limiar}:")
print(colunas_selecionadas)

df_Numerico_Final = df_Numerico_Relevantes[colunas_selecionadas]

X_cr = df_Numerico_Final.drop('MH7A', axis=1)
y_cr = df_Numerico_Final['MH7A']

y_cr.value_counts()

X_train, X_test, y_train, y_test = train_test_split(X_cr, y_cr, test_size=0.2, random_state=42)

from imblearn.over_sampling import SMOTE


smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

X_train_res = pd.DataFrame(X_train_res, columns=X_train.columns)


y_train_res.value_counts().plot.pie( autopct='%.2f')

"""###Random Forest"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix, classification_report

# Treinamento
modelo_rf = RandomForestClassifier(random_state=42)
modelo_rf.fit(X_train_res, y_train_res)

# Previsão
y_pred_rf = modelo_rf.predict(X_test)

# Avaliação
print("=== RANDOM FOREST ===")
print("Acurácia:", accuracy_score(y_test, y_pred_rf))
print("Recall:", recall_score(y_test, y_pred_rf))
print("\nMatriz de Confusão:")
cm = confusion_matrix(y_test, y_pred_rf)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Previsão')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()

"""###Rede Neural (MLPClassifier)"""

from sklearn.neural_network import MLPClassifier

modelo_mlp = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation='relu',
    solver='adam',
    max_iter=500,
    random_state=42,
 )
modelo_mlp.fit(X_train_res, y_train_res)

# Previsão
y_pred_mlp = modelo_mlp.predict(X_test)

# Avaliação
print("=== REDE NEURAL (MLP) ===")
print("Acurácia:", accuracy_score(y_test, y_pred_mlp))
print("Recall:", recall_score(y_test, y_pred_mlp))
print("\nMatriz de Confusão:")
# Gera a matriz de confusão
cm = confusion_matrix(y_test, y_pred_mlp)
# Exibe visualmente
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Previsão')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()

"""###Gradient Boosting"""

from sklearn.ensemble import GradientBoostingClassifier

# Treinamento
modelo_gb = GradientBoostingClassifier(random_state=42)
modelo_gb.fit(X_train_res, y_train_res)

# Previsão
y_pred_gb = modelo_gb.predict(X_test)

# Avaliação
print("=== GRADIENT BOOSTING ===")
print("Acurácia:", accuracy_score(y_test, y_pred_gb))
print("Recall:", recall_score(y_test, y_pred_gb))
print("\nMatriz de Confusão:")
cm = confusion_matrix(y_test, y_pred_gb)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Previsão')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()

"""##Usando o PCA"""

X_crpca = df_Numerico_Final.drop('MH7A', axis=1)
y_crpca = df_Numerico_Final['MH7A']

from sklearn.decomposition import PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_crpca)

pca = PCA(n_components=5, random_state=42)
X_pca = pca.fit_transform(X_scaled)

X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42, stratify=y)

smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

"""###Random Forest"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

modelo_rf = RandomForestClassifier(random_state=42)
modelo_rf.fit(X_train_res, y_train_res)
y_pred_rf = modelo_rf.predict(X_test)

print("=== RANDOM FOREST ===")
print("Acurácia:", accuracy_score(y_test, y_pred_rf))
print("Recall:", recall_score(y_test, y_pred_rf))

cm = confusion_matrix(y_test, y_pred_rf)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title("Matriz de Confusão - Random Forest")
plt.xlabel("Previsão")
plt.ylabel("Real")
plt.show()

"""###Rede Neural ( MLPclassifier)"""

from sklearn.neural_network import MLPClassifier

modelo_mlp = MLPClassifier(random_state=42, max_iter=300)
modelo_mlp.fit(X_train_res, y_train_res)
y_pred_mlp = modelo_mlp.predict(X_test)

print("=== REDE NEURAL (MLP) ===")
print("Acurácia:", accuracy_score(y_test, y_pred_mlp))
print("Recall:", recall_score(y_test, y_pred_mlp))
cm = confusion_matrix(y_test, y_pred_mlp)
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', cbar=False)
plt.title("Matriz de Confusão - MLPClassifier")
plt.xlabel("Previsão")
plt.ylabel("Real")
plt.show()

"""###Gradient Boosting"""

from sklearn.ensemble import GradientBoostingClassifier

modelo_gb = GradientBoostingClassifier(random_state=42)
modelo_gb.fit(X_train_res, y_train_res)
y_pred_gb = modelo_gb.predict(X_test)

print("=== GRADIENT BOOSTING ===")
print("Acurácia:", accuracy_score(y_test, y_pred_gb))
print("Recall:", recall_score(y_test, y_pred_gb))
cm = confusion_matrix(y_test, y_pred_gb)
sns.heatmap(cm, annot=True, fmt='d', cmap='Oranges', cbar=False)
plt.title("Matriz de Confusão - Gradient Boosting")
plt.xlabel("Previsão")
plt.ylabel("Real")
plt.show()

