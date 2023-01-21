from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

df = pd.read_csv('C:\\Users\Robert\Documents\winequelity.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = Dash(__name__)

app.layout = html.Div([
    generate_table(df),
    html.Br(),
    html.Label('Choose model:'),
    dcc.Dropdown(['Regression', 'Classification'], 'Regression', id='method-dropdown'),
    html.Br(),
    html.Label('Choose variable'),
    dcc.Dropdown(df.columns.to_list(), 'fixed acidity', id='var-dropdown'),
    dcc.Graph(id='graph', figure={})
])


@callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='method-dropdown', component_property='value'),
     Input(component_id='var-dropdown', component_property='value')]
)
def create_graph(model, var):
    if model == 'Regression':
        fig = px.area(df, y="pH", x=var)
    if model == 'Classification':
        fig = px.area(df, x="target", y=var)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
