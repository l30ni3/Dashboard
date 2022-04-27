from dash.testing.application_runners import import_app
import requests
import json
from app import getData
import unittest.mock as mock
import pandas as pd

def test_graph_ui_exitsts(dash_duo):
    app = import_app("test.app")
    dash_duo.start_server(app)
    assert dash_duo.find_element("#graph")
    dash_duo.percy_snapshot("graph")

def test_table_ui_exists(dash_duo):
    app = import_app("test.app")
    dash_duo.start_server(app)
    assert dash_duo.find_element("#table")
    dash_duo.percy_snapshot("table")

def test_request_data(dash_duo):
    # obtain data from ckan API
    gov_requests = requests.get(
        "https://www.govdata.de/ckan/api/3/action/organization_list?all_fields=true&sort=package_count%20desc"
    )
    assert gov_requests.status_code == 200

def test_read_from_json(dash_duo):
    ministries = []
    # flatten the list of all ministry names to consider
    with open("departments.json", encoding='utf-8') as departments:
        json_dep = json.load(departments)
        for i in json_dep['departments']:
            ministries.append(i.get('name'))
            if i.get('subordinates'):
                for sub in i['subordinates']:
                    ministries.append(sub.get('name'))
        departments.close()
    assert len(ministries) == 30