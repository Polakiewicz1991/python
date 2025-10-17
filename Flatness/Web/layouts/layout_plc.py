from dash import html, dcc
from Flatness.Web.layouts.buttons import get_buttons
from Flatness.Web.layouts.translations import translations

def get_plc_layout(lang='pl'):
    tr = translations.get(lang, translations['pl'])

    button_with_process_icon, button_with_up_icon, button_with_down_icon = get_buttons(lang)

    style_table_referenceNames = {
        'border': '1px solid black',
        'borderCollapse': 'collapse',
        'width': '600px',
        'tableLayout': 'fixed',
        'position': 'relative',
        'marginTop': '20px',
    }

    style_table_referenceActive = {
        'border': '2px solid black',
        'borderCollapse': 'collapse',
        'width': '300px',
        'tableLayout': 'fixed',
    }

    style_table_referenceNextToActive = {
        'border': '2px solid black',
        'borderCollapse': 'collapse',
        'width': '300px',
        'tableLayout': 'fixed',
    }

    style_table_map_right = {
        'border': '1px solid black',
        'borderCollapse': 'collapse',
        'width': '300px',
        'tableLayout': 'fixed',
        'marginLeft': '20px',
    }

    style_td = {'height': '40px', 'fontSize': '24px'}

    # Kontener dla dwóch tabel referencji obok siebie:
    container_two_tables_style = {
        'display': 'flex',
        'flexDirection': 'row',
        'justifyContent': 'space-between',
        'width': '100%',
        'maxWidth': '650px',
        'marginBottom': '20px',
    }

    buttons_column_style = {
        'display': 'flex',
        'flexDirection': 'column',
        'justifyContent': 'space-between',
        'height': '600px',
    }

    right_side_container_style = {
        'display': 'flex',
        'flexDirection': 'row',
        'justifyContent': 'start',
        'alignItems': 'flex-start',
        'gap': '10px',
        'marginTop': '20px',
    }

    return html.Div([
        html.H2(tr['tab_plc'], style={'marginBottom': '20px'}),

        dcc.Interval(id='interval-plc', interval=1000, n_intervals=0),
        dcc.Store(id='val_CONTROLiReferenceShow', data=0),

        # Dwie tabele referencji obok siebie
        html.Div([
            html.Table([
                html.Thead(html.Tr([html.Th(tr['active_reference'], style={'width': '300px', 'fontSize': '18px'})])),
                html.Tbody([
                    html.Tr([
                        html.Td(id='val-sReferenceActive', style=style_td)
                    ])
                ])
            ], style=style_table_referenceActive),

            html.Table([
                html.Thead(html.Tr([html.Th(tr['next_reference'], style={'width': '300px', 'fontSize': '18px'})])),
                html.Tbody([
                    html.Tr([
                        html.Td(id='val-sReferenceNextToActive', style=style_td)
                    ])
                ])
            ], style=style_table_referenceNextToActive),
        ], style=container_two_tables_style),

        # Tabela referenceNames z przyciskami po prawej ORAZ nowa tabela po prawej stronie
        html.Div([
            # Lewa część: tabela referenceNames i przyciski
            html.Div([
                html.Table([
                    html.Thead(html.Tr([
                        html.Th(tr['lp'], style={'width': '30px', 'fontSize': '18px'}),
                        html.Th(tr['value'], style={'width': '580px', 'fontSize': '18px'}),
                    ])),
                    html.Tbody([
                        html.Tr(id=f'row_{i}',
                                children=[
                                    html.Td(f"{i + 1}.", style=style_td),
                                    html.Td(id=f'val-sReferenceNames_{i}', style=style_td)
                                ]
                            ) for i in range(14)
                    ]),
                ], style=style_table_referenceNames),
                html.Div([
                    button_with_up_icon,
                    button_with_process_icon,
                    button_with_down_icon,
                ], style=buttons_column_style),
            ], style={'display': 'flex', 'flexDirection': 'row', 'gap': '10px'}),

            # Prawa część: nowa tabela z podanymi polami
            html.Table([
                html.Thead(html.Tr([
                    html.Th(tr['selected_reference'], style={'width': '300px','fontSize': '18px'}),
                    html.Th("", style={'width': '300px','fontSize': '18px'}),
                ])),
                html.Tbody([
                    html.Tr([html.Td(tr['reference_name'], style=style_td), html.Td(id='val_MAPsName', style=style_td)]),
                    html.Tr([html.Td(tr['system'], style=style_td), html.Td(id='val_MAPstTableParamiSYSTEM', style=style_td)]),
                    html.Tr([html.Td(tr['length'], style=style_td), html.Td(id='val_MAPstTableParamrDIMENSION_X', style=style_td)]),
                    html.Tr([html.Td(tr['width'], style=style_td), html.Td(id='val_MAPstTableParamrDIMENSION_Y', style=style_td)]),
                    html.Tr([html.Td(tr['height'], style=style_td), html.Td(id='val_MAPstTableParamrDIMENSION_Z', style=style_td)]),
                ])
            ], style=style_table_map_right),
        ], style=right_side_container_style),
    ])