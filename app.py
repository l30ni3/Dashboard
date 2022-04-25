from dash import Dash, html, dash_table
import pandas as pd
import requests

categories=["display_name","package_count"]
app = Dash(__name__)

gov_requests = requests.get(
    "https://www.govdata.de/ckan/api/3/action/organization_list?all_fields=true&sort=package_count%20desc"
)

json_data = gov_requests.json()
df = pd.DataFrame(json_data.get('result'))

# Iterate over all the items in dictionary and filter items which appear in departments.json
print (df.columns)
print (categories)

app.layout = html.Div(children=[
    html.H1(children='GovData Dashboard'),

    html.Div(children='''
        A small web application that provides information about how many data sets each federal ministry has made available on GovData.
    '''),

    dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in categories])
     
]) 

if __name__ == '__main__':
    app.run_server(debug=True)