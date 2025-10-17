from dash import html, dcc
from Flatness.Web.layouts.translations import translations


def get_layout():
    return html.Div([
        html.Div(id='tabs-container', children=[
            dcc.Tabs(id='tabs', value='tab-wykresy', children=[])
        ]),
        # Pasek zakładek + język
        html.Div([
            html.Div(id='tabs-container'),  # <-- tu będą dynamiczne zakładki

            dcc.Dropdown(
                id='language-selector',
                options=[
                    {'label': '🇵🇱 Polski', 'value': 'pl'},
                    {'label': '🇩🇪 Deutsch', 'value': 'de'},
                    {'label': '🇬🇧 English', 'value': 'en'}
                ],
                value='pl',
                clearable=False,
                style={
                    'width': '150px',
                    'marginLeft': '20px',
                    'alignSelf': 'center'
                }
            )
        ], style={
            'display': 'flex',
            'alignItems': 'center',
            'gap': '20px',
            'marginBottom': '20px'
        }),

        # Zawartość zakładek
        html.Div(id='tabs-content')
    ])