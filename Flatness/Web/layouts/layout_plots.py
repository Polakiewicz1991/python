from dash import html, dcc
from Flatness.Web.layouts.translations import translations

def get_3d_plots_layout(lang='pl'):
    tr = translations.get(lang, translations['pl'])

    return html.Div([
        html.H2(tr['upload_csv']),
        html.Div([
            dcc.Upload(
                id='upload-data',
                children=html.Button(tr['browse_upload'])
            ),
            html.Button(tr['reset_view'], id='reset-view-btn', n_clicks=0)
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