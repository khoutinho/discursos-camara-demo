def evolucao_temporal(df):
    return df.groupby('Ano').size().reset_index(name='Total')

def distribuicao_espectro(df):
    return df.groupby(['Ano', 'Espectro']).size().reset_index(name='Count')

def top_partidos(df, n=10):
    return df['Partido'].value_counts().head(n).reset_index()
