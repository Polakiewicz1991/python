from dash import html, dcc

button_with_process_icon = html.Button([
    html.Img(
        src="../assets/processColor.svg",
        alt="process",
        style={
            'width': '100px',
            'height': '100px',
            'padding': '5px',
            'marginRight': '2px'
        }
    ),
    html.Span(
        "Aktywuj",
        style={
            'display': 'inline-block',  # żeby transformacja działała poprawnie
            'transform': 'rotate(270deg)',
            'transformOrigin': 'center center',  # punkt obrotu można dostosować według potrzeby
            'whiteSpace': 'nowrap',
            'lineHeight': 'normal',
            'fontSize': '25px',
            'marginLeft': '0px',
            'marginTop': '0px',
            'marginRight': '0px'
        }
    )
], style={'display': 'flex', 'alignItems': 'center'}, id='btn-CONTROLbActive')

button_with_up_icon = html.Button([
    html.Img(
        src="../assets/ArrowUpColor.svg",
        alt="process",
        style={
            'width': '100px',
            'height': '100px',
            'padding': '5px',
            'marginRight': '2px'
        }
    ),
    html.Span(
        "W gore",
        style={
            'display': 'inline-block',  # żeby transformacja działała poprawnie
            'transform': 'rotate(270deg)',
            'transformOrigin': 'center center',  # punkt obrotu można dostosować według potrzeby
            'whiteSpace': 'nowrap',
            'lineHeight': 'normal',
            'fontSize': '25px',
            'marginLeft': '0px',
            'marginTop': '0px',
            'marginRight': '0px'
        }
    )
], style={'display': 'flex', 'alignItems': 'center'}, id='btn-CONTROLbDisplayUp')

button_with_down_icon = html.Button([
    html.Img(
        src="../assets/ArrowDownColor.svg",
        alt="process",
        style={
            'width': '100px',
            'height': '100px',
            'padding': '5px',
            'marginRight': '2px'
        }
    ),
    html.Span(
        "W dol",
        style={
            'display': 'inline-block',  # żeby transformacja działała poprawnie
            'transform': 'rotate(270deg)',
            'transformOrigin': 'center center',  # punkt obrotu można dostosować według potrzeby
            'whiteSpace': 'nowrap',
            'lineHeight': 'normal',
            'fontSize': '25px',
            'marginLeft': '0px',
            'marginTop': '0px',
            'marginRight': '0px'
        }
    )
], style={'display': 'flex', 'alignItems': 'center'}, id='btn-CONTROLbDisplayDown')