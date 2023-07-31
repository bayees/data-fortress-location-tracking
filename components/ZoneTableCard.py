from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import dcc, callback
import numpy as np
import plotly.express as px
import pandas as pd
from dotenv import load_dotenv
import os
import dash_mantine_components as dmc

load_dotenv()

ZoneTableCard = html.Div(
    className="col-md-12 col-lg-12 mb-md-0 mb-4 card-chart-container",
    children=[
        html.Div(
            className="card",
            children=[
                dbc.Row(
                    [
                        dbc.Col(
                            className="col-lg-6",
                            children=[
                                html.Div(
                                    className="card-header card-m-0 me-2 pb-3",
                                    children=[
                                        html.H2(
                                            ["Personal position tracking"],
                                            className="card-title m-0 me-2 mb-2",
                                            style={"font-size": "1.5vw"},
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="card-body",
                                    children=[
                                        html.P(
                                            "Select location"
                                        ),
                                        dmc.Table(id='table', children=[]),
                                    ],
                                    style={"margin": "5px"}
                                )
                                
                            ],
                        ),
                    ]
                ),
            ],
        )
    ],
)


def create_table(df):
    columns, values = df.columns, df.values
    header = [html.Tr([html.Th(col) for col in columns])]
    rows = [html.Tr([html.Td(cell) for cell in row]) for row in values]
    table = [html.Thead(header), html.Tbody(rows)]
    return table

# Define the callback functions
@callback(
    Output('table', 'children'),
    Input('url', 'pathname'),
    Input("date-range-picker", "value"),
    Input("location-select", "value"),
    State("position-df" , "data"),
)
def update_plot(pathname, date_range, location_choice, position_data):
    position_df = pd.read_json(position_data)

    position_df = position_df[['date_actual', 'location_of_interest', 'duration_minutes']]
    position_df['date_actual'] = pd.to_datetime(position_df['date_actual'])
    
    position_df = position_df.loc[position_df['location_of_interest'].isin(location_choice)]

    position_df = position_df.loc[(position_df['date_actual'] >= date_range[0]) & (position_df['date_actual'] <= date_range[1])]

    position_df = position_df.groupby(['date_actual','location_of_interest']).sum().reset_index()

    position_df['duration_hours'] = round(position_df['duration_minutes']/60, 2)

    table = create_table(position_df)

    return table