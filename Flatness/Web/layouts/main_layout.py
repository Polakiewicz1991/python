from dash import html, dcc

def get_layout():
    # Zakładki i kontener na content
    return html.Div([
        dcc.Tabs(id='tabs', value='tab-wykresy', children=[
            dcc.Tab(label='Wykresy 3D', value='tab-wykresy'),
            dcc.Tab(label='Dane komunikacji PLC', value='tab-plc'),
        ]),
        html.Div(id='tabs-content', style={'marginTop': '20px'})
    ])