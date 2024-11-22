# Problema que Resolvemos
A situação dos oceanos está preocupante, pois ele está enfrentando sérios problemas de poluição, sendo evidente a existência de plásticos, produtos químicos, entre outros. Isso impacta negativamente as comunidades costeiras que dependem dos oceanos para sua subsistência e a biodiversidade marítima. Com isso, há uma falta de acessibilidade nos dados e compreensão dos mesmos sobre os efeitos dessa poluição, dificultando a conscientização e a implementação de soluções eficazes.

# Solução proposta
Este programa facilita a interpretação de dados já existentes. O usuário precisa apenas ter uma tabela feita e selecionar os dados que deseja comparar. O projeto visa melhorar a visualização de tabelas para que o usuário possa tirar conclusões mais rapidamente e com menos trabalho, fornecendo insights sobre o crescimento das fontes de energia renováveis em diferentes países ao longo dos anos.

# Requisitos
- Ter uma tabela com os dados que deseja manipular (exemplo: um arquivo `.csv` com informações sobre consumo de energia renovável).
- Ter o Python instalado na máquina.
- Instalar as bibliotecas necessárias: Pandas e Matplotlib.
    ```bash
    pip install pandas matplotlib
    ```
- Ter o Visual Studio Code (ou outro editor de sua preferência) instalado.

# Instruções de Uso
1. Clique em "Run Python File" no canto superior direito do seu editor (exemplo: Visual Studio Code).
   ![image](https://github.com/ViniMata/python_Global_Solutions/assets/123563801/40789374-6f8c-4a1a-9b31-48f3abebdd6f)
2. Assim que o código for executado, insira o caminho do seu arquivo `.csv` quando solicitado.

# Integrantes do Grupo
- Giovanne Charelli - RM 556223
- Vinicius Matareli - RM 555200

# Como o Código Funciona
O código realiza as seguintes etapas:

1. **Carregar dados**: O arquivo `.csv` contendo informações sobre consumo de energia renovável é carregado usando a biblioteca Pandas.
2. **Filtragem dos dados**: O usuário pode filtrar os dados por países e/ou intervalo de anos.
3. **Análise do crescimento**: O programa analisa o crescimento da energia renovável (como energia hidrelétrica) nos países selecionados.
4. **Exibição de insights**: O programa exibe o país com o maior crescimento médio no uso de energia renovável e outros insights relacionados.
5. **Gráfico de consumo**: Um gráfico é gerado para mostrar a evolução do consumo de energia renovável ao longo dos anos nos países selecionados.

### Exemplo de Execução:

```python
# Arquivo CSV contendo os dados sobre consumo de energia renovável
arquivo = "modern-renewable-energy-consumption.csv"

# Coluna de interesse (por exemplo, "Hydro generation - TWh")
coluna_energia = "Hydro generation - TWh"

# Países para análise (exemplo: Brasil e Argentina)
paises = ["Brazil", "Argentina"]

# Intervalo de anos
ano_inicio = 2013
ano_fim = 2023

# Executa o código
main(arquivo, coluna_energia, paises=paises, ano_inicio=ano_inicio, ano_fim=ano_fim)
