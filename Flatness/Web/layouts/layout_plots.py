from dash import html, dcc
from Flatness.Web.layouts.translations import translations

def get_3d_plots_layout(lang='pl'):
    tr = translations.get(lang, translations['pl'])

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

    return html.Div([
        # Nagłówek sekcji
        html.H2(
            tr['upload_csv'],
            style={
                'marginBottom': '25px',
                'fontSize': '26px',
                'fontWeight': '600',
                'textAlign': 'left',
            }
        ),
        dcc.Interval(
            id='interval-update',
            interval=30 * 1000,  # 30 sekund w milisekundach
            n_intervals=0
        ),

        # Sekcja upload + reset
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
        ], style={
            'display': 'flex',
            'gap': '14px',
            'alignItems': 'center',
            'marginBottom': '25px',
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

        # Sekcja wykresów 3-kolumnowa
        html.Div([
            # Lewa kolumna – zdublowane małe wykresy
            html.Div([
                html.Div([
                    dcc.Graph(id='chart_side_X1', style={'height': '295px', 'width': '100%'})
                ], style={**card_style, 'marginBottom': '10px'}),
                html.Div([
                    dcc.Graph(id='chart_side_Y1', style={'height': '295px', 'width': '100%'})
                ], style=card_style)
            ], style={'flex': '1', 'display': 'flex', 'flexDirection': 'column', 'marginRight': '15px'}),

            # Środkowa kolumna – główny wykres
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='chart_plate',
                        style={'height': '600px', 'width': '100%'}
                    )
                ], style=card_style)
            ], style={'flex': '3'}),

            # Prawa kolumna – oryginalne małe wykresy
            html.Div([
                html.Div([
                    dcc.Graph(id='chart_side_X2', style={'height': '295px', 'width': '100%'})
                ], style={**card_style, 'marginBottom': '10px'}),
                html.Div([
                    dcc.Graph(id='chart_side_Y2', style={'height': '295px', 'width': '100%'})
                ], style=card_style)
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