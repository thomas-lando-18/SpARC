"""
Coming Soon...
"""

from dash import Dash, dcc, html, Output, Input, callback

from simulator_tab import get_simulator_tab

TAB_STYLE = {
                    'fontFamily': 'Arial, Helvetica, sans-serif',
                    "fontSize": "15pt",
                    "color": "#ECECEC",
                    "background": "#737373"
                }

SELECTED_TAB_STYLE = {
                    'fontFamily': 'Arial, Helvetica, sans-serif',
                    "fontSize": "16pt",
                    "color": "white",
                    "background": "#737373"
                }
def app_main():

    app = Dash(__name__)

    # App layout
    app.layout = html.Div(
        children=[
            get_header_component(),
            get_tabs_component(),
            html.Div(id="header-tabs-content")
        ]
    )

    app.run(debug=True)

def get_header_component() -> html.Div:

    header = html.Div(
        children=[
            html.H1(
                "Space And Rocketry Calculator (SpARC)",
                style={
                    'fontFamily': 'Arial, Helvetica, sans-serif',
                    "fontSize": "20pt",
                    "color": "white",
                    
                }
                )
        ],
        style={
            "background": "#7D0000",
            "top": "0%",
            "right": "0%",
            "left": "0%",
            "position": "absolute",
            "paddingLeft": "10pt",
            "height": "7%",
        }
    )

    return header

def get_tabs_component() -> html.Div:

    tabs = html.Div(
        children=[
            dcc.Tabs(
                id='header-tabs',
                value='header-tabs',
                children=[
                    dcc.Tab(
                        label="Simulator",
                        value='sim',
                        style=TAB_STYLE,
                        selected_style=SELECTED_TAB_STYLE
                    ),
                    dcc.Tab(
                        label="Rocket",
                        value='rocket',
                        style=TAB_STYLE,
                        selected_style=SELECTED_TAB_STYLE
                    ),
                    dcc.Tab(
                        label="Location",
                        value='location',
                        style=TAB_STYLE,
                        selected_style=SELECTED_TAB_STYLE
                    ),
                    dcc.Tab(
                        label="Settings",
                        value='setting',
                        style=TAB_STYLE,
                        selected_style=SELECTED_TAB_STYLE
                    )
                ],
                style={
                    "paddingLeft": "0%",
                    "position": "fixed",
                    "paddingRight": "0%",
                    "width": "100vw",
                    "left": "0",
                    "right": "0"
                }
            ),
        ],
        style={
                    "postition": "fixed",
                    "paddingTop": "3.3%",
                    "width": '100vw',
                    "left": "0",
                    "right":  '0'
                }
        
    )

    return tabs

@callback(Output('header-tabs-content', 'children'),
              Input('header-tabs', 'value'))
def tab_switchboard(tab):

    if tab == 'sim':
        return get_simulator_tab()
    else: 
        return


if __name__ == '__main__':
    app_main()