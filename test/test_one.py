import dash
from dash import html
from dash.testing.application_runners import import_app

def test_layout(dash_duo):
    app = import_app("app.py")
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("h1", "Hello Dash", timeout=4)

    
