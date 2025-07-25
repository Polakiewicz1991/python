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

def get_plc_layout():

    button_with_process_icon = html.Button([
        html.Img(src="../assets/processColor.svg", alt="process", style={'height': '20px', 'marginRight': '8px'}),
        "Aktywuj"
    ], style={'display': 'flex', 'alignItems': 'center'}
    , id='btn-CONTROLbActive')

    style_table = {
        'border': '1px solid black',
        'borderCollapse': 'collapse',
        'width': '800px',
        'tableLayout': 'fixed',
    }
    style_td = {'height': '40px'}

    container_style = {
        'display': 'flex',
        'flexDirection': 'row',
        'alignItems': 'flex-start',  # wyrównanie w pionie na górze
        'gap': '10px',  # odstęp między tabelą a kolumną przycisków
    }

    buttons_column_style = {
        'display': 'flex',
        'flexDirection': 'column',
        'justifyContent': 'space-between',  # jeden przycisk na górze, drugi na dole
        'height': '600px',  # wysokość zgodna mniej więcej z tabelą
        'marginLeft': '10px'
    }

    button_style = {
        'width': '50px',
        'height': '50px',
        'padding': '5px',
        'border': '1px solid #ccc',
        'backgroundColor': '#f8f8f8',
        'cursor': 'pointer'
    }

    return html.Div([
        html.H2("Dane komunikacji PLC"),
        dcc.Interval(id='interval-plc', interval=1000, n_intervals=0),
        dcc.Store(id='val_CONTROLiSelectedRef', data=0),

#NIE MA PODSWIETLENIA i odniesien do


        html.Div([
            html.Table([
                html.Thead(html.Tr([
                    html.Th("Lp.", style={'width': '200px'}),
                    html.Th("Wartość", style={'width': '300px'}),
                ])),
                html.Tbody([
                    html.Tr(
                        id=f'row_{i}',
                        children=[
                            html.Td(f"{i + 1}.", style=style_td),
                            html.Td(id=f'val-sReferenceNames_{i}', style=style_td)
                        ]
                    ) for i in range(14)
                ]),
            ], style=style_table),

            html.Div([
                html.Button([
                    html.Img(src='../assets/ArrowUpColor.svg', alt='Top', style={'width': '40px', 'height': '40px'})
                ], id='btn-top', style=button_style),

                html.Button([
                    html.Img(src='../assets/ArrowDownColor.svg', alt='Bottom', style={'width': '40px', 'height': '40px'})
                ], id='btn-bottom', style=button_style),

            ], style=buttons_column_style)
        ], style=container_style),






        html.Div([
        html.Table([
            html.Thead(html.Tr([
                html.Th("Nazwa", style={'width': '200px'}),
                html.Th("Wartość", style={'width': '300px'}),
                html.Th(style={'width': '100px'})
            ])),
            html.Tbody([
                html.Tr([
                    html.Td("sReferenceActive", style={'height': '40px'}),
                    html.Td(id='val-sReferenceActive', style={'height': '40px'}),
                    # html.Td(html.Button('Ustaw Referencje', id='btn-CONTROLbActive'),
                    #         style={'height': '40px', 'textAlign': 'center'})
                    html.Td(button_with_process_icon)
                ]),
                html.Tr([
                    html.Td("sReferenceNextToActive", style={'height': '40px'}),
                    html.Td(id='val-sReferenceNextToActive', style={'height': '40px'}),
                    html.Td(),  # brak przycisku dla tej zmiennej
                ]),
                html.Tr([
                    html.Td("bBlinker_1000ms", style={'height': '40px'}),
                    html.Td(id='val-bBlinker_1000ms', style={'height': '40px'}),
                    html.Td()
                ])
            ])
        ], style={
            'border': '1px solid black',
            'borderCollapse': 'collapse',
            'width': '800px',
            'tableLayout': 'fixed',
            'position': 'fixed',
            'bottom': '10px',    # 10px od dołu okna
            'left': '10px'       # 10px od lewej krawędzi okna
            })
        ])
    ])

