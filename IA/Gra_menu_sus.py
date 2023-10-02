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
        options=[{'label': categoria, 'value': categoria} for categoria in df['category'].unique()],
        multi=True,
        value=[]  # Inicialmente, nenhum filtro está selecionado
    ),
    dcc.Graph(id='bar-plot')
])

# Callback para atualizar o gráfico com base nas categorias selecionadas
@app.callback(
    Output('bar-plot', 'figure'),
    Input('categoria-dropdown', 'value')
)
def update_bar_plot(selected_categories):
    if not selected_categories:
        return px.bar()

    filtered_df = df[df['category'].isin(selected_categories)]
    contagem_categorias = filtered_df['category'].value_counts().reset_index()
    contagem_categorias.columns = ['Categoria', 'Número de Clientes']

    paleta_cores = px.colors.qualitative.Set1

    fig = px.bar(contagem_categorias, x='Categoria', y='Número de Clientes', title='Número de Clientes por Categoria',
                 color='Categoria', color_discrete_sequence=paleta_cores)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
