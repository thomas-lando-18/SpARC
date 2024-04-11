"""
Coming Soon...
"""

from dash import Dash, dcc, html, Output, Input, callback

from simulator_tab import get_simulator_tab

from constants import TAB_STYLE, SELECTED_TAB_STYLE


def app_main():

    app = Dash(__name__, title="SpARC", update_title="Loading...")

    # App layout
    app.layout = html.Div(
        children=[
            get_header_component(),
            get_tabs_component(),
            html.Div(id="header-tabs-content"),
        ]
    )

    app.run(debug=True, host="localhost")


def get_header_component() -> html.Div:

    header = html.Div(
        children=[
            html.H1(
                "Space And Rocketry Calculator (SpARC)",
                style={
                    "fontFamily": "Arial, Helvetica, sans-serif",
                    "fontSize": "3vh",
                    "color": "white",
                },
            )
        ],
        style={
            "background": "#7D0000",
            "top": "0",
            "right": "0",
            "left": "0",
            "position": "fixed",
            "paddingLeft": "1vw",
            "height": "7vh",
        },
    )

    return header


def get_tabs_component() -> html.Div:

    tabs = html.Div(
        children=[
            dcc.Tabs(
                id="header-tabs",
                value="header-tabs",
                children=[
                    dcc.Tab(
                        label="Geographic",
                        value="geo",
                        style=TAB_STYLE,
                        selected_style=SELECTED_TAB_STYLE,
                    ),
                    dcc.Tab(
                        label="Simulator",
                        value="sim",
                        style=TAB_STYLE,
                        selected_style=SELECTED_TAB_STYLE,
                    ),
                    dcc.Tab(
                        label="Rocket",
                        value="rocket",
                        style=TAB_STYLE,
                        selected_style=SELECTED_TAB_STYLE,
                    ),
                    dcc.Tab(
                        label="Location",
                        value="location",
                        style=TAB_STYLE,
                        selected_style=SELECTED_TAB_STYLE,
                    ),
                    dcc.Tab(
                        label="Settings",
                        value="setting",
                        style=TAB_STYLE,
                        selected_style=SELECTED_TAB_STYLE,
                    ),
                ],
                style={
                    "position": "fixed",
                    "top": "7vh",
                    "left": "0",
                    "right": "0",
                    "height": "7vh",
                },
            ),
        ],
        style={
            "postition": "fixed",
            "top": "7vh",
            "height": "7vh",
            "left": "0",
            "right": "0",
        },
    )

    return tabs


@callback(Output("header-tabs-content", "children"), Input("header-tabs", "value"))
def tab_switchboard(tab):

    if tab == "sim":
        return get_simulator_tab()
    else:
        return html.Div(
            style={
                "position": "fixed",
                "left": "0",
                "right": "0",
                "top": "14vh",
                "bottom": "0",
                "backgroundColor": "#2F2F2F",
            }
        )


if __name__ == "__main__":
    app_main()
