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

# Transformar colunas
colunas_ordinais = [
    'W1','W2','W3', 'W4', 'W5A','W5B','W5C', 'W5D','W5E','W5F','W5G','W6','W7A','W7B', 'W7C','W8','W9','W11A',
    'W14','W11B', 'W30', 'age_mh', 'Household_Income',
    'MH1', 'MH2A', 'MH2B', 'MH3B', 'MH4B', 'MH5', 'MH6', 'MH3A','MH3B','MH3C','MH3D',
    'MH4A','MH4B','MH5','MH9A','MH9B', 'MH9C', 'MH9D', 'MH9E', 'MH9F',
    'MH9G','MH9H','W28','W29', 'age_mh', 'wbi', 'subjective_Income'
]

colunas_nominais = ['COUNTRYNEW','MH7B_2','EMP_2010']
colunas_booleanas = ['MH6','MH7A','MH7C','MH8A','MH8B','MH8C','MH8D','MH8E','MH8F','MH8G','MH8H','W27']

# Processar colunas ordinais
for col in colunas_ordinais:
    if col in df_SulAmerica_util.columns:
        df_SulAmerica_util[col] = df_SulAmerica_util[col].replace([' ', '', '99', 99], np.nan)
        df_SulAmerica_util[col] = pd.to_numeric(df_SulAmerica_util[col], errors='coerce')

# Processar colunas booleanas
for col in colunas_booleanas:
    if col in df_SulAmerica_util.columns:
        df_SulAmerica_util[col] = df_SulAmerica_util[col].astype(str).str.strip()
        df_SulAmerica_util[col] = df_SulAmerica_util[col].replace({
            '1': 1, '2': 0, '99': np.nan, '99.0': np.nan, '': np.nan, 'nan': np.nan
        })
        df_SulAmerica_util[col] = pd.to_numeric(df_SulAmerica_util[col], errors='coerce')
        df_SulAmerica_util[col] = df_SulAmerica_util[col].astype('Int64')

# One-hot encoding para colunas nominais
df_Numerico = pd.get_dummies(df_SulAmerica_util, columns=colunas_nominais, dummy_na=False)

# Converter colunas booleanas para float
colunas_Onehot = df_Numerico.select_dtypes(include='bool').columns
df_Numerico[colunas_Onehot] = df_Numerico[colunas_Onehot].astype('float')

# Remover colunas com muitos valores nulos
colunas_remover_2 = ['MH9D','MH9A','MH9B', 'MH9F', 'MH8G', 'age_mh',
                     'MH8H', 'MH8E', 'MH7C','MH8B','MH8C', 'MH8D',
                     'MH8A', 'MH9G','MH9G', 'MH9E', 'MH9C', 'MH7B', 'MH8F', 'MH9H']

df_Numerico_Relevantes = df_Numerico.drop(columns=colunas_remover_2)
df_Numerico_Relevantes = df_Numerico_Relevantes.apply(pd.to_numeric, errors='coerce').astype('float64')

# Tratar valores nulos
for col in df_Numerico_Relevantes.columns:
    if df_Numerico_Relevantes[col].isnull().sum() > 0:
        media = df_Numerico_Relevantes[col].mean()
        media_arredondada = round(media)
        df_Numerico_Relevantes[col] = df_Numerico_Relevantes[col].fillna(media_arredondada)

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

# Salvar as colunas usadas no treinamento
joblib.dump(X.columns.tolist(), 'feature_columns.joblib')

print("Modelo treinado e salvo com sucesso!") 