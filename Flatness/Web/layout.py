from dash import html, dcc

def get_layout():
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
