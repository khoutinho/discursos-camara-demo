import pandas as pd

ESPECTRO = {
    'PT': 'Esquerda',
    'PSOL': 'Esquerda',
    'PCdoB': 'Esquerda',
    'MDB': 'Centro',
    'PSD': 'Centro-direita',
    'PL': 'Direita',
    'PP': 'Direita',
    'REPUBLICANOS': 'Direita',
}

UF_REGIAO = {
    'SP': 'Sudeste',
    'RJ': 'Sudeste',
    'MG': 'Sudeste',
    'RS': 'Sul',
    'PR': 'Sul',
    'BA': 'Nordeste',
    'GO': 'Centro-Oeste',
    'PA': 'Norte'
}

def load_and_clean(path):
    df = pd.read_csv(path)

    df['Data_dt'] = pd.to_datetime(df['Data'], errors='coerce')
    df['Ano'] = df['Data_dt'].dt.year

    df = df.dropna(subset=['Ano'])

    df['Espectro'] = df['Partido'].map(ESPECTRO).fillna("Não classificado")
    df['Regiao'] = df['Estado'].map(UF_REGIAO).fillna("Não identificado")

    return df
