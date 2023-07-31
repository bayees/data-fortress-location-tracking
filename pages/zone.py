from dash import html
import dash_bootstrap_components as dbc
from components.ZoneTableCard import ZoneTableCard
from components.ZoneStatsOverall import ZoneStatsOverall

zone_page_content = html.Div([
    dbc.Row(
        ZoneStatsOverall,
    ),
    dbc.Row([
        ZoneTableCard,
    ]),
], style={"padding-top": "0px"})
