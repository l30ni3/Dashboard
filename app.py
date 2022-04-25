from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import requests

app = Dash(__name__)

gov_requests = requests.get(
    "https://www.govdata.de/ckan/api/3/action/organization_list?all_fields=true&sort=package_count%20desc"
)

json_data = gov_requests.json()
df = pd.DataFrame(json_data)
print (df)

app.layout = html.Div(children=[
    html.H1(children='GovData Dashboard'),

    html.Div(children='''
        A small web application that provides information about how many data sets each federal ministry has made available on GovData.
    '''),
])

if __name__ == '__main__':
    app.run_server(debug=True)