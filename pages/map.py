from dash import html
import dash_bootstrap_components as dbc
from components.MapCard import MapCard
from components.MapStatsOverall import MapStatsOverall

map_page_content = html.Div([
    dbc.Row(
        MapStatsOverall,
    ),
    dbc.Row([
        MapCard,
    ]),
], style={"padding-top": "0px"})
