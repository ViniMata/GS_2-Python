import pandas as pd
import matplotlib.pyplot as plt

#Função que lê e coloca em tabelas os codigos:
def importar_e_filtrar():
    df = pd.read_csv("modern-renewable-energy-consumption.csv")

    paises = df['Entity'].unique()
    tabelas_por_paises = {pais : df[df['Entity'] == pais] for pais in paises}

    return df, tabelas_por_paises

df, tabelas_por_paises = importar_e_filtrar()

def escolha_de_colunas():
    print("Segue as colunas: 'Solar generation - TWh | Wind generation - TWh | Hydro generation - TWh'")

    print("Copie e cole")

    coluna_escolhida = str(input("Qual coluna você quer as informações?"))
    return coluna_escolhida

coluna_escolhida = escolha_de_colunas()



for pais in tabelas_por_paises:
    # Filtra o DataFrame do país atual e plota os dados ao longo do tempo
    dados_pais = tabelas_por_paises[pais]
    
    # Verifica se a coluna específica existe para o país
    if coluna_escolhida in dados_pais.columns:
        plt.plot(dados_pais['Year'], dados_pais[coluna_escolhida], label=pais)
        
        plt.xlabel('Years')
        plt.ylabel('Valor')
        plt.title(f'Comparação de {coluna_escolhida} de {pais}')
        plt.legend()
        plt.show()
