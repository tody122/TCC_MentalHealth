import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import joblib

# Carregar e pré-processar os dados
df = pd.read_csv("Mentalhealth.csv", low_memory=False)

# Filtrar países sul-americanos
paises_sul_americanos = [
    'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia',
    'Ecuador', 'Paraguay', 'Peru', 'Uruguay', 'Venezuela'
]

df_SulAmericanos = df[df['COUNTRYNEW'].isin(paises_sul_americanos)]

# Remover colunas desnecessárias
colunas_remover = ['WPID_RANDOM', 'FIELD_DATE', 'PROJWT', 'WGT',
                  'YEAR_WAVE','Global11Regions','age_var1',
                  'age_var2', 'Age','WP21757', 'WP21758',
                  'WP21759', 'WP21760', 'WP21761', 'WP21768',
                  'W10', 'W13', 'W14', 'W15',
                  'W15_1A', 'W15_1B', 'W15_1C',
                  'W15_1D','W15_1E','W15_2A', 'W15_2B','W30']

df_SulAmerica_util = df_SulAmericanos.drop(columns=colunas_remover)

# Pré-processamento dos dados
# ... (adicionar todo o pré-processamento necessário)

# Preparar dados para treinamento
X = df_Numerico_Relevantes.drop(columns=['MH7A'])
y = df_Numerico_Relevantes['MH7A']

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Aplicar SMOTE para balancear as classes
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Criar e treinar o pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('kbest', SelectKBest(k=12)),
    ('model', RandomForestClassifier(random_state=42))
])

pipeline.fit(X_train_res, y_train_res)

# Salvar o modelo e o scaler
joblib.dump(pipeline, 'model.joblib')
joblib.dump(pipeline.named_steps['scaler'], 'scaler.joblib')

print("Modelo treinado e salvo com sucesso!") 