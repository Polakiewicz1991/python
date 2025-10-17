from dash import html, dcc
from Flatness.Web.layouts.translations import translations
from Flatness.Web.layouts.layout_plc import get_plc_layout

def get_layout():
    return html.Div([
        # Kontener flex - w wierszu obok siebie
        html.Div([
            dcc.Tabs(id='tabs', value='tab-wykresy', children=[
                dcc.Tab(label='Wykresy 3D', value='tab-wykresy'),
                dcc.Tab(label='Dane komunikacji PLC', value='tab-plc'),
            ], style={'flexGrow': '1'}),  # rozszerz zakładki na ile się da

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
                    'alignSelf': 'center'  # wyśrodkowanie pionowe w linii
                }
            )
        ], style={
            'display': 'flex',
            'alignItems': 'center',  # pionowe wyrównanie do środka
            'gap': '20px',  # odstęp między zakładkami a dropdownem
            'marginBottom': '20px'  # odstęp od treści pod spodem
        }),

        # Kontener na treść zakładek
        html.Div(id='tabs-content')
    ])

