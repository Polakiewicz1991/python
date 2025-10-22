from dash import html, dcc
from Flatness.Web.layouts.translations import translations

def get_3d_plots_layout(lang='pl'):
    tr = translations.get(lang, translations['pl'])

    DEFAULT_FOLDER_PATH = r"E:\PP\23_0005_0000 - Portal pomiarowy do stołów\Dokumentacja"

    # --- Style bazowe spójne z layoutem PLC ---
    card_style = {
        'backgroundColor': '#ffffff',
        'boxShadow': '0 2px 6px rgba(0,0,0,0.1)',
        'borderRadius': '10px',
        'padding': '20px',
        'flex': '1',
    }

    button_style = {
        'backgroundColor': '#1890ff',
        'color': 'white',
        'border': 'none',
        'borderRadius': '8px',
        'padding': '10px 18px',
        'fontSize': '15px',
        'fontWeight': '600',
        'cursor': 'pointer',
        'transition': 'all 0.2s ease',
        'boxShadow': '0 1px 3px rgba(0,0,0,0.1)',
    }

    upload_style = {
        'border': '2px dashed #d9d9d9',
        'borderRadius': '10px',
        'padding': '14px 22px',
        'textAlign': 'center',
        'cursor': 'pointer',
        'transition': 'border-color 0.3s ease',
        'backgroundColor': '#fafafa',
        'fontWeight': '500',
    }

    # --- Dropdown dla częstotliwości ---
    refresh_dropdown = dcc.Dropdown(
        id='refresh-interval',
        options=[
            {'label': f'{v} s', 'value': v} for v in [1, 2, 5, 10, 15, 30, 60]
        ],
        value=30,  # domyślnie 30 sekund
        clearable=False,
        style={'width': '100px'}
    )

    # przycisk do wyboru folderu
    folder_button = html.Button(
        tr.get('select_folder', '📁 Wybierz folder'),
        id='select-folder-btn',
        n_clicks=0,
        style=button_style
    )

    # pole tekstowe z aktualną ścieżką
    folder_input = dcc.Input(
        id='folder-input',
        type='text',
        value=DEFAULT_FOLDER_PATH,  # np. wczytanie domyślnej ścieżki
        style={'width': '400px'}
    )

    folder_label = html.Div(
        id='current-folder-label',
        children=DEFAULT_FOLDER_PATH,
        style={
            'marginLeft': '10px',
            'fontSize': '14px',
            'color': '#555',
            'maxWidth': '600px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
            'whiteSpace': 'nowrap'
        }
    )

    return html.Div([
        html.H2(
            tr['upload_csv'],
            style={
                'marginBottom': '25px',
                'fontSize': '26px',
                'fontWeight': '600',
                'textAlign': 'left',
            }
        ),

        # 🟡 Interval (będzie aktualizowany przez dropdown)
        dcc.Interval(id='interval-update', interval=30 * 1000, n_intervals=0),

        # 🔷 Sekcja upload + reset + refresh + folder
        html.Div([
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    html.I(className='fa fa-upload', style={'marginRight': '8px'}),
                    tr['browse_upload']
                ]),
                style=upload_style,
            ),
            html.Button(
                tr['reset_view'],
                id='reset-view-btn',
                n_clicks=0,
                style=button_style
            ),
            html.Div([
                html.Span("⏱ ", style={'marginRight': '4px'}),
                refresh_dropdown
            ], style={'display': 'flex', 'alignItems': 'center', 'gap': '5px'}),

            html.Div([
                folder_input,
                folder_button
                #folder_label
            ], style={'display': 'flex', 'alignItems': 'center', 'gap': '8px'})
        ], style={
            'display': 'flex',
            'gap': '14px',
            'alignItems': 'center',
            'marginBottom': '25px',
            'flexWrap': 'wrap'
        }),

        # Wynik płaskości
        html.Div(
            id='flatness-output',
            style={
                'fontWeight': '600',
                'marginBottom': '20px',
                'fontSize': '16px',
                'color': '#333'
            }
        ),

        # --- Sekcja wykresów ---
        html.Div([
            html.Div([
                html.Div([dcc.Graph(id='chart_side_X1', style={'height': '295px', 'width': '100%'})],
                         style={**card_style, 'marginBottom': '10px'}),
                html.Div([dcc.Graph(id='chart_side_Y1', style={'height': '295px', 'width': '100%'})],
                         style=card_style)
            ], style={'flex': '1', 'display': 'flex', 'flexDirection': 'column', 'marginRight': '15px'}),

            html.Div([
                html.Div([dcc.Graph(id='chart_plate', style={'height': '600px', 'width': '100%'})],
                         style=card_style)
            ], style={'flex': '3'}),

            html.Div([
                html.Div([dcc.Graph(id='chart_side_X2', style={'height': '295px', 'width': '100%'})],
                         style={**card_style, 'marginBottom': '10px'}),
                html.Div([dcc.Graph(id='chart_side_Y2', style={'height': '295px', 'width': '100%'})],
                         style=card_style)
            ], style={'flex': '1', 'display': 'flex', 'flexDirection': 'column', 'marginLeft': '15px'}),
        ], style={
            'display': 'flex',
            'width': '100%',
            'alignItems': 'flex-start',
        }),

    ], style={
        'padding': '30px',
        'maxWidth': '1500px',
        'margin': '0 auto',
        'fontFamily': 'Segoe UI, Arial, sans-serif',
        'backgroundColor': '#fafafa',
        'borderRadius': '12px',
    })