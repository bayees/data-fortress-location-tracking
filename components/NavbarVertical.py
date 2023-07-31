from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.Div(
            [
                html.Img(src="./assets/images/navbar_icon.png", style={"width": "3rem"}),
                html.H4("Location", className="m-0"),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className="tf-icons bx bx-home fas fa-home"), 
                        html.Span("Home" , className="me-2")
                    ],
                    href="/",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink(
                    [
                        html.I(className="tf-icons bx bx-map-alt fas fa-map"), 
                        html.Span("Map", className="me-2"),
                    ],
                    href="/map",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink(
                    [
                        html.I(className="tf-icons bx bx-map-pin fas fa-map"), 
                        html.Span("Zone", className="me-2"),
                    ],
                    href="/zone",
                    active="exact",
                    className="pe-3"
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar bg-menu-theme",
)