import pandas as pd
import plotly.express as px

# Especifique o caminho para o arquivo CSV
caminho_arquivo_csv = r'C:\Users\015545\Desktop\Banco\Dados\Dados analíticos de funil.csv'

# Carregue o arquivo CSV em um DataFrame
df = pd.read_csv(caminho_arquivo_csv)

# Use a função value_counts para contar o número de clientes por categoria
contagem_categorias = df['category'].value_counts().reset_index()
contagem_categorias.columns = ['Categoria', 'Número de Clientes']

# Defina uma paleta de cores personalizada
paleta_cores = px.colors.qualitative.Set1  # Você pode escolher outra paleta de cores se preferir

# Crie um gráfico de barras interativo usando o Plotly e especifique a paleta de cores
fig = px.bar(contagem_categorias, x='Categoria', y='Número de Clientes', title='Número de Clientes por Categoria',
             color='Categoria', color_discrete_sequence=paleta_cores)

# Exiba o gráfico no navegador
fig.show()
