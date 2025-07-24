from dash import html, dcc

def get_3d_plots_layout():
    return html.Div([
        html.H2("Wczytaj plik CSV z danymi 3D (x;y;z)"),
        html.Div([
            dcc.Upload(
                id='upload-data',
                children=html.Button('Przeglądaj i załaduj CSV')
            ),
            html.Button("Resetuj widok", id='reset-view-btn', n_clicks=0)
        ], style={'display': 'flex', 'gap': '10px', 'alignItems': 'center', 'marginBottom': '20px'}),
        html.Div(id='flatness-output', style={'fontWeight': 'bold', 'marginBottom': '20px'}),
        html.Div([
            html.Div([dcc.Graph(id='three-d-plot-1', style={'height': '600px', 'width': '100%'})], style={'flex': '3', 'marginRight': '10px'}),
            html.Div([
                dcc.Graph(id='three-d-plot-2', style={'height': '295px', 'width': '100%', 'marginBottom': '10px'}),
                dcc.Graph(id='three-d-plot-3', style={'height': '295px', 'width': '100%'})
            ], style={'flex': '1', 'display': 'flex', 'flexDirection': 'column'})
        ], style={'display': 'flex', 'width': '100%'})
    ])

def get_plc_data_layout():
    # Przykładowy widok danych PLC - możesz tu podstawić własne komponenty
    return html.Div([
        html.H2("Dane komunikacji PLC"),
        html.Table([
            html.Thead(html.Tr([html.Th("Adres"), html.Th("Stan"), html.Th("Wartość")])),
            html.Tbody([
                html.Tr([html.Td("GP3000H-DUPS-01"), html.Td("OK"), html.Td("123.45")]),
                html.Tr([html.Td("PLC2"), html.Td("Błąd połączenia"), html.Td("-")]),
            ])
        ], style={'border': '1px solid black', 'borderCollapse': 'collapse', 'width': '50%'})
    ])

def get_layout():
    # Zakładki i kontener na content
    return html.Div([
        dcc.Tabs(id='tabs', value='tab-wykresy', children=[
            dcc.Tab(label='Wykresy 3D', value='tab-wykresy'),
            dcc.Tab(label='Dane komunikacji PLC', value='tab-plc'),
        ]),
        html.Div(id='tabs-content', style={'marginTop': '20px'})
    ])

def get_plc_layout():
    return html.Div([
        html.H2("Dane komunikacji PLC"),
        dcc.Interval(id='interval-plc', interval=1000, n_intervals=0),
        html.Table([
            html.Thead(html.Tr([html.Th("Nazwa"), html.Th("Wartość")])),
            html.Tbody([
                html.Tr([
                    html.Td("sReferenceActive"),
                    html.Td(id='val-sReferenceActive')
                ]),
                html.Tr([
                    html.Td("sReferenceNextToActive"),
                    html.Td(id='val-sReferenceNextToActive')
                ]),
                html.Tr([
                    html.Td("bBlinker_1000ms"),
                    html.Td(id='val-bBlinker_1000ms')
                ])
            ])
        ], style={'border': '1px solid black', 'borderCollapse': 'collapse', 'width': '40%', 'marginTop': '10px'})
    ])
