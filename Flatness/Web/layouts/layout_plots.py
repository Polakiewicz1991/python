from dash import html, dcc
from Flatness.Web.layouts.translations import translations

def get_3d_plots_layout(lang='pl'):
    tr = translations.get(lang, translations['pl'])
    DEFAULT_FOLDER_PATH = r"E:\PP\23_0005_0000 - Portal pomiarowy do stołów\Dokumentacja"

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

    # Dropdown dla częstotliwości odświeżania
    refresh_dropdown = dcc.Dropdown(
        id='refresh-interval',
        options=[{'label': f'{v} s', 'value': v} for v in [1, 2, 5, 10, 15, 30, 60]],
        value=30,
        clearable=False,
        style={'width': '100px'}
    )

    # Przycisk do wyboru folderu
    folder_button = html.Button(
        tr.get('select_folder', '📁 Wybierz folder'),
        id='select-folder-btn',
        n_clicks=0,
        style=button_style
    )

    # przycisk bistabilny
    interval_toggle_btn = html.Button(
        "Start",
        id='interval-toggle-btn',
        n_clicks=0,
        style={**button_style, 'backgroundColor': '#52c41a'}  # zielony
    )

    # Pole tekstowe z aktualną ścieżką
    folder_input = dcc.Input(
        id='folder-input',
        type='text',
        value=DEFAULT_FOLDER_PATH,
        style={'width': '400px'}
    )

    # H2
    header = html.H2(
        tr['upload_csv'],
        style={'marginBottom': '25px', 'fontSize': '26px', 'fontWeight': '600', 'textAlign': 'left'}
    )

    # Interval Dash
    interval = dcc.Interval(id='interval-update', interval=30*1000, n_intervals=0)

    # 🔷 Upload + Reset (górny wiersz)
    top_row = html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([html.I(className='fa fa-upload', style={'marginRight': '8px'}), tr['browse_upload']]),
            style=upload_style
        ),
        html.Button(tr['reset_view'], id='reset-view-btn', n_clicks=0, style=button_style)
    ], style={'display': 'flex', 'gap': '14px', 'marginBottom': '10px'})

    # 🔷 Wiersz wybór folderu + interwał
    folder_row = html.Div([
        folder_button,
        interval_toggle_btn,
        html.Div([html.Span("⏱", style={'marginRight': '4px'}), refresh_dropdown],
                 style={'display': 'flex', 'alignItems': 'center', 'gap': '5px'}),
        folder_input
    ], style={'display': 'flex', 'gap': '14px', 'marginBottom': '25px', 'alignItems': 'center'})

    # Wynik płaskości
    flatness_output = html.Div(id='flatness-output',
                               style={'fontWeight': '600', 'marginBottom': '20px', 'fontSize': '16px', 'color': '#333'})

    # Sekcja wykresów (3 kolumny)
    plots = html.Div([
        # Lewa kolumna
        html.Div([
            html.Div(dcc.Graph(id='chart_side_X1', style={'height': '295px', 'width': '100%'}),
                     style={**card_style, 'marginBottom': '10px'}),
            html.Div(dcc.Graph(id='chart_side_Y1', style={'height': '295px', 'width': '100%'}),
                     style=card_style)
        ], style={'flex': '1', 'display': 'flex', 'flexDirection': 'column', 'marginRight': '15px'}),

        # Środkowa kolumna
        html.Div([
            html.Div(dcc.Graph(id='chart_plate', style={'height': '600px', 'width': '100%'}), style=card_style)
        ], style={'flex': '3'}),

        # Prawa kolumna
        html.Div([
            html.Div(dcc.Graph(id='chart_side_X2', style={'height': '295px', 'width': '100%'}),
                     style={**card_style, 'marginBottom': '10px'}),
            html.Div(dcc.Graph(id='chart_side_Y2', style={'height': '295px', 'width': '100%'}),
                     style=card_style)
        ], style={'flex': '1', 'display': 'flex', 'flexDirection': 'column', 'marginLeft': '15px'}),
    ], style={'display': 'flex', 'width': '100%', 'alignItems': 'flex-start'})

    return html.Div([header, interval, top_row, folder_row, flatness_output, plots],
                    style={'padding': '30px', 'maxWidth': '1500px', 'margin': '0 auto',
                           'fontFamily': 'Segoe UI, Arial, sans-serif', 'backgroundColor': '#fafafa',
                           'borderRadius': '12px'})
