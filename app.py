from dash import Dash, html, dcc, dash_table
import pandas as pd
import requests
import json
from dash.dependencies import Input, Output
import plotly.express as px

titles=["Name","Datasets"]
categories=["display_name","package_count"]
ministries = []


app = Dash(__name__)

def getData():
    data = []
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
    return df.to_dict('records')

app.layout = html.Div([
    dcc.Interval('table-update', interval = 300*1000, n_intervals = 0),

    html.Div([
        dcc.Graph(id='graph')
    ]),
    
    dash_table.DataTable(
          id = 'table',
          data = getData(),
            columns= [{"name": i, "id": i} for i in categories]),

]) 

# callback to update data every 5 minutes
@app.callback(Output('table','data'), [Input('table-update', 'n_intervals')])
def updateTable(n):
    return getData()

@app.callback(Output('graph', 'figure'), [Input('table-update', 'n_intervals')])
def update_graph(my_dropdown):
    df=getData()
    pie = px.pie(df, values='package_count', names='display_name', title='GovData Dashboard')
    pie.update_traces(textposition='inside')
    pie.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    return(pie)


if __name__ == '__main__':
    app.run_server(debug=True)