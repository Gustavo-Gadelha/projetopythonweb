from dash import Dash, html

app = Dash(__name__)
server = app.server

app.layout = html.Div(children=[
    html.H1('Meu projeto'),
    html.Div(html.A('Olá mundo!'))
])

if __name__ == '__main__':
    app.run_server(debug=True)
