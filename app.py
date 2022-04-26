from dash import Dash, html, dcc
import pandas as pd
import requests
import json
from dash.dependencies import Input, Output

titles=["Name","Provided datasets"]
categories=["display_name","package_count"]
ministries = []
data = []

app = Dash(__name__)

def generate_table():
    # obtain data from ckan API
    gov_requests = requests.get(
        "https://www.govdata.de/ckan/api/3/action/organization_list?all_fields=true&sort=package_count%20desc"
    )
    json_data = gov_requests.json()

    # flatten the list of all ministry names to consider
    with open("departments.json", encoding='utf-8') as departments:
        json_dep = json.load(departments)
        for i in json_dep['departments']:
            ministries.append(i.get('name'))
            if i.get('subordinates'):
                for sub in i['subordinates']:
                    ministries.append(sub.get('name'))
        departments.close()

    # only consider the API results, that appear in the departments.json
    for result in json_data.get('result'):
        if result['display_name'] in ministries:
            data.append(result)

    # create data frame
    df = pd.DataFrame(data)
    
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in titles])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in categories
            ]) for i in range(len(df))
        ])
    ])

app.layout = html.Div([
    dcc.Interval(
            id='interval',
            interval=300*1000,
            n_intervals=0
        ),

    html.H1('GovData Dashboard'),

    html.Div('''
        A small web application that provides information about how many data sets each federal ministry has made available on GovData.
    ''', style={'marginBottom': 20}),

    html.Div([
        html.Div(id="gov_data", children=generate_table()
        )
    ]),
]) 

# callback to update data every 5 minutes
@app.callback(Output("gov_data", "children"), [Input("interval", "n_intervals")])
def update_data_div(n):
    return generate_table()()


if __name__ == '__main__':
    app.run_server(debug=True)