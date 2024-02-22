from dash import dcc, html


def get_simulator_tab():
    
    sim_tab = html.Div(
        children=[
            html.P("This tab holds the simulator", style={"top": '50vh', 'position': 'fixed'})
        ]
    )
    
    return sim_tab
