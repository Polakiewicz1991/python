from dash import html, dcc
from Flatness.Web.layouts.buttons import button_with_process_icon, button_with_up_icon, button_with_down_icon

def get_plc_layout():
    style_table_referenceNames = {
        'border': '1px solid black',
        'borderCollapse': 'collapse',
        'width': '600px',
        'tableLayout': 'fixed',
        'position': 'relative',  # lub pominąć wcale
        'marginTop': '20px',
    }

    style_table_referenceActive = {
        'border': '2px solid black',
        'borderCollapse': 'collapse',
        'width': '300px',
        'tableLayout': 'fixed',
        # usunięte 'position:fixed'!
    }

    style_table_referenceNextToActive = {
        'border': '2px solid black',
        'borderCollapse': 'collapse',
        'width': '300px',
        'tableLayout': 'fixed',
        # usunięte 'position:fixed'!
    }

    style_td = {'height': '40px','fontSize': '24px'}

    # Kontener dla dwóch tabel referencji obok siebie:
    container_two_tables_style = {
        'display': 'flex',
        'flexDirection': 'row',
        'justifyContent': 'space-between',
        'width': '100%',
        'maxWidth': '650px',  # takie minimum, możesz dostosować
        'marginBottom': '20px'
    }

    # Kontener dla tabeli referenceNames z przyciskami po prawej
    container_referenceNames_style = {
        'display': 'flex',
        'flexDirection': 'row',
        'alignItems': 'flex-start',
        'gap': '10px'
    }

    buttons_column_style = {
        'display': 'flex',
        'flexDirection': 'column',
        'justifyContent': 'space-between',
        'height': '600px',  # podepnij wysokość pod zawartość referenceNames
    }


    button_style = {
        'width': '100px',
        'height': '100px',
        'padding': '5px',
        'border': '1px solid #ccc',
        'backgroundColor': '#f8f8f8',
        'cursor': 'pointer'
    }

    return html.Div([
        # Napis zaraz pod zakładkami
        html.H2("Dane komunikacji PLC", style={'marginBottom': '20px'}),

        dcc.Interval(id='interval-plc', interval=1000, n_intervals=0),
        dcc.Store(id='val_CONTROLiReferenceShow', data=0),#[PLC1]GVL_Reference.CONTROL.iReferenceShow

        # Dwie tabele referencji obok siebie
        html.Div([
            # Aktywna referencja - po prawej
            html.Table([
                html.Thead(html.Tr([html.Th("Aktywna referencja", style={'width': '300px','fontSize': '18px'})])),
                html.Tbody([
                    html.Tr([
                        html.Td(id='val-sReferenceActive', style={'height': '40px', 'fontSize': '24px'})
                    ])
                ])
            ], style=style_table_referenceActive),

            # Następna referencja - po lewej
            html.Table([
                html.Thead(html.Tr([html.Th("Następna referencja", style={'width': '300px', 'fontSize': '18px'})])),
                html.Tbody([
                    html.Tr([
                        html.Td(id='val-sReferenceNextToActive', style={'height': '40px', 'fontSize': '24px'})
                    ])
                ])
            ], style=style_table_referenceNextToActive),
        ], style=container_two_tables_style),

        # Tabela referenceNames z przyciskami po prawej
        html.Div([
            html.Table([
                html.Thead(html.Tr([
                    html.Th("Lp.", style={'width': '30px','fontSize': '18px'}),
                    html.Th("Wartość", style={'width': '580px','fontSize': '18px'}),
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
                button_with_down_icon

            ], style=buttons_column_style),

        ], style=container_referenceNames_style),

        # Opcjonalnie przycisk z ikoną „Aktywuj” (jeśli chcesz dodać go gdzieś)
        # html.Div(button_with_process_icon, style={'marginTop': '20px'}),

    ])