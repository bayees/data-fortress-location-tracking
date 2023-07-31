from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
from dash import callback
from dash.dependencies import Input, Output, State
from utils.consts import positions
import datetime
import dash_mantine_components as dmc

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
                                            style={"width": 230},
                                            inputFormat="YYYY-MM-DD",
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


total_budget_card = html.Div(
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

MapStatsOverall = [
        period_select_card,
        total_budget_card,
        total_expense_card,
        difference_card,
    ]

@callback(
    Output("latest-transaction-text", "children"),
    Input("date-range-picker", "value"),
    State("position-df", "data"),
)
def update_team_select(date_range, position_data):
    position_df = pd.read_json(position_data)
    position_df['date_actual'] = pd.to_datetime(position_df['date_actual'])
    position_df = position_df.loc[(position_df['date_actual'] >= date_range[0]) & (position_df['date_actual'] <= date_range[1])]

    latest_transaction = f"Latest transaction: : {position_df.date_actual.max()}"

    return latest_transaction,
