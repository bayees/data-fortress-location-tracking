from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from dash import callback
from dash.dependencies import Input, Output, State
from utils.consts import positions
import datetime
import dash_mantine_components as dmc
from dateutil.relativedelta import *

period_select_card = html.Div(
    className="col-lg-3 col-md-6 col-sm-12 card-chart-container",
    children=[
        html.Div(
            className="card",
            children=[
                html.Div(
                    className="card-body",
                    children=[
                        html.Div(
                            className="d-flex justify-content-between",
                            children=[
                                html.Div(
                                    className="card-info",
                                    children=[
                                        dmc.DateRangePicker(
                                            id="date-range-picker",
                                            label="Date Range",
                                            minDate=positions.date_actual.min(),
                                            maxDate=positions.date_actual.max(),
                                            value=[positions.date_actual.max() -  datetime.timedelta(days=5), positions.date_actual.max()],
                                            style={"width": 240},
                                            inputFormat="YYYY-MM-DD",
                                        ),
                                        dmc.Stack(
                                            dmc.ChipGroup(
                                                [dmc.Chip(x, value=x) for x in ['This month', 'Last month']],
                                                value="This month",
                                                id="period-select",
                                            ),
                                            align="flex-start",
                                            style={"margin-top": "10px"},
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="card-icon d-flex align-items-center w-40 justify-content-center p-1",
                                    children=[
                                        html.Img(
                                            className="img-fluid bx-lg",
                                            id="team-flag-main",
                                            src="./assets/images/calendar.png",
                                            style={
                                                "width": "2.5em",
                                            },
                                        ),
                                    ],
                                ),
                            ],
                        )
                    ],
                )
            ],
            style={"min-height": "11rem"},
        )
    ],
)

location_card = html.Div(
    html.Div(
        className="card",
        children=[
            html.Div(
                className="card-body",
                    children=[
                        html.Div(
                            className="d-flex justify-content-between",
                            children=[
                                html.Div(
                                    className="card-info",
                                    children=[
                                        dmc.MultiSelect(
                                            id='location-select',
                                            label="Location",
                                            data=[{'label':x , 'value':x} for x in positions.location_of_interest.unique()],
                                            value=[],
                                            clearable=True,
                                            style={"width": 230},
                                            placeholder="Select location",
                                        )
                                    ],
                                ),
                                html.Div(
                                    className="card-icon d-flex align-items-center w-40 justify-content-center p-1",
                                    children=[
                                        html.Img(
                                            className="img-fluid bx-lg",
                                            id="team-flag-main",
                                            src="./assets/images/map-pin.png",
                                            style={
                                                "width": "2.5em",
                                            },
                                        ),
                                    ],
                                ),
                            ],
                        )
                    ],
            )
        ],
        style={"min-height": "11rem"},
    ),
    className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container",
)

total_expense_card = html.Div(
    html.Div(
        className="card",
        children=[
            html.Div(
                className="card-body",
                children=[
                    
                ],
            )
        ],
        style={"min-height": "11rem"},
    ),
    className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container",
)

difference_card = html.Div(
    html.Div(
        className="card",
        children=[
            html.Div(
                className="card-body",
                children=[
                ],
            )
        ],
        style={"min-height": "11rem"},
    ),
    className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container",
)

ZoneStatsOverall = [
        period_select_card,
        location_card,
        total_expense_card,
        difference_card,
    ]

def last_day_of_month(date):
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month+1, day=1) - datetime.timedelta(days=1)

# Define the callback functions
@callback(
    Output('date-range-picker', 'value'),
    Input("period-select", "value"),
)
def update_plot(period):
    date = datetime.datetime.today()

    if period == 'Last month':   
        date = date - relativedelta(months=+1)
        return [date.replace(day=1), last_day_of_month(date)]

    return [date.replace(day=1), last_day_of_month(date)]