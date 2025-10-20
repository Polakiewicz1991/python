from dash import html, dcc
from Flatness.Web.layouts.buttons import get_buttons
from Flatness.Web.layouts.translations import translations

def get_plc_layout(lang='pl'):
    tr = translations.get(lang, translations['pl'])
    button_with_process_icon, button_with_up_icon, button_with_down_icon = get_buttons(lang)

    # Style ogólne
    card_style = {
        'backgroundColor': '#ffffff',
        'boxShadow': '0 2px 6px rgba(0,0,0,0.1)',
        'borderRadius': '10px',
        'padding': '16px',
        'flex': '1',
        'minWidth': '300px',
    }

    table_style = {
        'width': '100%',
        'borderCollapse': 'collapse',
        'textAlign': 'left',
    }

    th_style = {
        'padding': '8px 12px',
        'fontSize': '16px',
        'borderBottom': '2px solid #ccc',
        'backgroundColor': '#f7f7f7',
        'textAlign': 'left',
    }

    td_style = {
        'padding': '8px 12px',
        'fontSize': '16px',
        'borderBottom': '1px solid #eee',
        'height': '40px',
    }

    # Przyciski — teraz 2× szersze
    buttons_column_style = {
        'display': 'flex',
        'flexDirection': 'column',
        'justifyContent': 'flex-start',
        'alignItems': 'stretch',
        'gap': '16px',
        'marginTop': '10px',
        'width': '200',   # <<< szerokość x2
    }

    return html.Div([
        html.H2(tr['tab_plc'], style={
            'marginBottom': '20px',
            'fontSize': '26px',
            'fontWeight': '600',
        }),

        dcc.Interval(id='interval-plc', interval=1000, n_intervals=0),
        dcc.Store(id='val_CONTROLiReferenceShow', data=0),

        # GÓRNA SEKCJA – dwie tabele referencji pod wspólnym nagłówkiem
        html.Div([
            html.Div([
                html.H3(tr['active_reference'], style={
                    'textAlign': 'center',
                    'marginBottom': '10px',
                    'fontWeight': '600',
                    'fontSize': '18px',
                }),
                html.Div([
                    html.Table([
                        html.Tbody([
                            html.Tr([
                                html.Td(id='val-sReferenceActive', style=td_style)
                            ])
                        ])
                    ], style=table_style)
                ], style=card_style),
            ], style={'flex': '1'}),

            html.Div([
                html.H3(tr['next_reference'], style={
                    'textAlign': 'center',
                    'marginBottom': '10px',
                    'fontWeight': '600',
                    'fontSize': '18px',
                }),
                html.Div([
                    html.Table([
                        html.Tbody([
                            html.Tr([
                                html.Td(id='val-sReferenceNextToActive', style=td_style)
                            ])
                        ])
                    ], style=table_style)
                ], style=card_style),
            ], style={'flex': '1'}),

        ], style={
            'display': 'flex',
            'gap': '20px',
            'alignItems': 'flex-start',
            'marginBottom': '30px',
        }),

        # DOLNA SEKCJA – tabele + szerokie przyciski po prawej
        html.Div([
            # Lewa część – dwie tabele (główna + parametry)
            html.Div([
                # Tabela referencji
                html.Div([
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th(tr['lp'], style=th_style),
                            html.Th(tr['value'], style=th_style),
                        ])),
                        html.Tbody([
                            html.Tr(
                                id=f'reference_row_{i}',  # <<< unikalne ID dla każdego wiersza
                                children=[
                                    html.Td(f"{i + 1}.", style=td_style),
                                    html.Td(id=f'val-sReferenceNames_{i}', style=td_style),
                                ],
                                style=td_style
                            ) for i in range(14)
                        ])
                    ], style=table_style)
                ], style={**card_style, 'flex': '1'}),

                # Tabela parametrów
                html.Div([
                    html.Table([
                        html.Thead(html.Tr([
                            html.Th(tr['selected_reference'], style=th_style),
                            html.Th("", style=th_style),
                        ])),
                        html.Tbody([
                            html.Tr([html.Td(tr['reference_name'], style=td_style), html.Td(id='val_MAPsName', style=td_style)]),
                            html.Tr([html.Td(tr['system'], style=td_style), html.Td(id='val_MAPstTableParamiSYSTEM', style=td_style)]),
                            html.Tr([html.Td(tr['length'], style=td_style), html.Td(id='val_MAPstTableParamrDIMENSION_X', style=td_style)]),
                            html.Tr([html.Td(tr['width'], style=td_style), html.Td(id='val_MAPstTableParamrDIMENSION_Y', style=td_style)]),
                            html.Tr([html.Td(tr['height'], style=td_style), html.Td(id='val_MAPstTableParamrDIMENSION_Z', style=td_style)]),
                        ])
                    ], style=table_style)
                ], style={**card_style, 'flex': '0.9'}),
            ], style={
                'display': 'flex',
                'flexDirection': 'row',
                'gap': '20px',
                'flex': '1',
                'minWidth': '0',
            }),

            # Prawa część – SZEROKIE PRZYCISKI
            html.Div([
                button_with_up_icon,
                button_with_process_icon,
                button_with_down_icon,
            ], style=buttons_column_style),

        ], style={
            'display': 'flex',
            'flexDirection': 'row',
            'justifyContent': 'space-between',
            'alignItems': 'flex-start',
            'gap': '20px',
            'width': '100%',
        }),

    ], style={
        'padding': '30px',
        'maxWidth': '1500px',   # zwiększona szerokość sekcji
        'margin': '0 auto',
        'fontFamily': 'Segoe UI, Arial, sans-serif',
        'backgroundColor': '#fafafa',
    })