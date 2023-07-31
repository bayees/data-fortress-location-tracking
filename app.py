import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__))))
if module_path not in sys.path:
    sys.path.append(module_path)

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
import pandas as pd
from components.NavbarVertical import sidebar
from components.Footer import Footer
from dash.dependencies import Input, Output, State
from pages.home import home_page_content
from pages.map import map_page_content
from pages.zone import zone_page_content
import glob
from utils.data import get_positions


# RAW
ROOT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__))))
SRC_FOLDER = os.path.join(ROOT_FOLDER, "/")
ASSETS_FOLDER = os.path.join(SRC_FOLDER, "assets/")

external_style_sheet = glob.glob(
    os.path.join(ASSETS_FOLDER, "bootstrap/css") + "/*.css"
)
external_style_sheet += glob.glob(os.path.join(ASSETS_FOLDER, "css") + "/*.css")
external_style_sheet += glob.glob(os.path.join(ASSETS_FOLDER, "fonts") + "/*.css")

app = dash.Dash(
    __name__,
    title="Position Tracking Dashboard",
    external_stylesheets=[dbc.themes.BOOTSTRAP] + external_style_sheet,
    suppress_callback_exceptions=True,
)

server = app.server

def serve_layout():
    # Processed
    position_df = get_positions()

    # Data Store for all the dataframes used in the app to avoid reading from server. Data is stored client side in JSON format.
    data_store = html.Div(
        [
            dcc.Store(id="position-df", data=position_df.to_json(date_format = 'iso')),
        ]
    )

    return html.Div(
        className="layout-wrapper layout-content-navbar",
        children=[
            html.Div(
                className="layout-container",
                children=[
                    dcc.Location(id="url"),
                    data_store,
                    html.Aside(className="", children=[sidebar]),
                    html.Div(
                        className="layout-page",
                        children=[
                            html.Div(
                                className="content-wrapper",
                                children=[
                                    html.Div(
                                        className="flex-grow-1 container-p-y p-0",
                                        id="page-content",
                                        children=[],
                                    ),
                                    html.Footer(
                                        className="content-footer footer bg-footer-theme",
                                        children=[Footer],
                                        style={"margin-left": "6rem"},
                                    ),
                                ],
                            )
                        ],
                    ),
                ],
            )
        ],
    )

app.layout = serve_layout

@callback(
    Output(component_id="page-content", component_property="children"),
    Input(component_id="url", component_property="pathname"),
)
def routing(path):
    if path == "/":
        return home_page_content
    elif path == "/map":
        return map_page_content
    elif path == "/zone":
        return zone_page_content

app.index_string = """<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
"""

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=5050, debug=True)
