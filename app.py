import pandas as pd
import matplotlib.pyplot as plt

#Função principal para carregar os dados
def carregar_dados(arquivo):
    df = pd.read_csv(arquivo)
    return df

#Função para filtrar os dados por paises e anos
def filtrar_dados(df, paises=None, ano_inicio = None, ano_fim=None):
    if paises:
        df = df[df['Entity'].isin(paises)]
    if ano_inicio and ano_fim:
        df = df[(df['Year'] >= ano_inicio) & (df['Year'] <= ano_fim)]
    return df

# Função para analisar o crescimento das fontes de energia
def analisar_crescimento(df, coluna_energia):
    def crescimento_por_pais(pais):
        dados_pais = df[df['Entity'] == pais]
        if not dados_pais.empty and coluna_energia in dados_pais.columns:
            crescimento = dados_pais[coluna_energia].pct_change().fillna(0)
            return crescimento.mean() #Traz a média do crescimento
        return 0
    
    return {pais: crescimento_por_pais(pais) for pais in df["Entity"].unique()}

# Função para trazer os insights
def obter_insights(df, coluna_energia):
    paises_crescimento = analisar_crescimento(df, coluna_energia)
    
    #País com maior crescimento
    pais_maior_crescimento = max(paises_crescimento, key=paises_crescimento.get)
    maior_crescimento = paises_crescimento[pais_maior_crescimento]

    #Exibe o resultado
    print(f"País com maior crescimento médio em {coluna_energia}:{pais_maior_crescimento} ({maior_crescimento:.2%})")
    return paises_crescimento

#Função para plotar o consumo de energia limpa ao longo dos anos
def plotar_energia(df, coluna_energia):
    for pais in df['Entity'].unique():
        dados_pais = df[df['Entity'] == pais]
        if coluna_energia in dados_pais.columns:
            plt.plot(dados_pais['Year'], dados_pais[coluna_energia], label=pais)

    plt.xlabel('Ano')
    plt.ylabel(coluna_energia)
    plt.title(f'Consumo de {coluna_energia} em vários países')
    plt.legend()
    plt.show()

# Função main
def main(arquivo, coluna_energia, paises=None, ano_inicio=None, ano_fim=None):

    #Carregar dado
    df = carregar_dados(arquivo)

    #Filtrar dados
    df_filtrado = filtrar_dados(df, paises=paises, ano_inicio=ano_inicio, ano_fim=ano_fim)

    #Exibir insights
    print("\nInsights sobre o crescimento de enrgia limpa:")
    obter_insights(df_filtrado, coluna_energia)

    # Plotar o consumo ao longo dos anos
    plotar_energia(df_filtrado, coluna_energia)

#Parametros de entrada
arquivo = "modern-renewable-energy-consumption.csv"
coluna_energia = "Hydro generation - TWh"  # Escolha de coluna
paises = ["Brazil","Argentina"]  # Exemplo de países
ano_inicio = 2013
ano_fim = 2023

# Executa
main(arquivo, coluna_energia, paises=paises, ano_inicio=ano_inicio, ano_fim=ano_fim)