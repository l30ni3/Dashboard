from dash import Dash, html
import pandas as pd
import requests
import json
import plotly.express as px

titles=["Name","Provided datasets"]
categories=["display_name","package_count"]
ministries = []
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

def generate_table(dataframe):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in titles])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in categories
            ]) for i in range(len(dataframe))
        ])
    ])

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1('GovData Dashboard'),

    html.Div('''
        A small web application that provides information about how many data sets each federal ministry has made available on GovData.
    ''', style={'marginBottom': 20}),

    generate_table(df)
]) 

if __name__ == '__main__':
    app.run_server(debug=True)