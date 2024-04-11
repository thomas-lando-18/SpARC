from dash import dcc, html


def get_simulator_tab():

    sim_tab = html.Div(
        children=[
            html.H1(
                children=["This tab holds the simulator"],
                style={
                    "top": "15vh",
                    "position": "fixed",
                    "paddingLeft": "1vw",
                    "color": "white",
                    "fontFamily": "Arial, Helvetica, sans-serif",
                    "fontSize": "2vh",
                },
            )
        ],
        style={
            "position": "fixed",
            "left": "0",
            "right": "0",
            "top": "14vh",
            "bottom": "0",
            "backgroundColor": "#2F2F2F",
        },
    )

    return sim_tab
