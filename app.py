from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='GovData Dashboard'),

    html.Div(children='''
        A small web application that provides information about how many data sets each federal ministry has made available on GovData.
    '''),
])

if __name__ == '__main__':
    app.run_server(debug=True)