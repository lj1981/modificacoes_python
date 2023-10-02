import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Carregue o arquivo CSV em um DataFrame
caminho_arquivo_csv = r'C:\Users\015545\Desktop\Banco\Dados\Dados analíticos de funil.csv'
df = pd.read_csv(caminho_arquivo_csv)

# Crie uma instância do aplicativo Dash
app = dash.Dash(__name__)

# Layout do aplicativo
app.layout = html.Div([
    dcc.Dropdown(
        id='categoria-dropdown',
        options=[
            {'label': 'Todas as Categorias', 'value': 'all_categories'}  # Opção para selecionar todas as categorias
        ] + [{'label': categoria, 'value': categoria} for categoria in df['category'].unique()],  # Categorias individuais
        multi=True,
        value=['all_categories']  # Defina 'all_categories' como valor inicial
    ),
    dcc.Graph(id='pie-plot')
])

    # Callback para atualizar o gráfico com base nas categorias selecionadas
@app.callback(
    Output('pie-plot', 'figure'),
    Input('categoria-dropdown', 'value')
)
def update_pie_plot(selected_categories):
    if 'all' in selected_categories or 'all_categories' in selected_categories:
        # Se 'Categorias' ou 'Selecionar Todas as Categorias' estiverem selecionadas, exiba o gráfico completo
        contagem_categorias = df['category'].value_counts().reset_index()
        contagem_categorias.columns = ['Categoria', 'Número de Clientes']
    else:
        filtered_df = df[df['category'].isin(selected_categories)]
        contagem_categorias = filtered_df['category'].value_counts().reset_index()
        contagem_categorias.columns = ['Categoria', 'Número de Clientes']

    paleta_cores = px.colors.qualitative.Set1

    fig = px.pie(contagem_categorias, values='Número de Clientes', names='Categoria', title='Número de Clientes por Categoria',
                 color='Categoria', color_discrete_sequence=paleta_cores)

    return fig

if __name__ == '__main__':
    app.run_server(debug=False)
