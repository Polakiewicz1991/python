from dash import html, dcc

def serve_layout(all_data):
    return html.Div([
        html.H1("CSV Comparison Tool", style={"textAlign": "center"}),

        html.Div([
            dcc.Dropdown(
                id="file-multi-dropdown",
                options=[{"label": f, "value": f} for f in all_data.keys()],
                multi=True,
                placeholder="Select CSV files to compare...",
                style={"width": "70%", "display": "inline-block", "marginRight": "10px"}
            ),
            html.Button(
                "Copy Selected",
                id="copy-button",
                n_clicks=0,
                style={
                    "display": "inline-block",
                    "backgroundColor": "#007bff",
                    "color": "white",
                    "border": "none",
                    "padding": "8px 15px",
                    "borderRadius": "5px",
                },
            ),
        ], style={"textAlign": "center", "marginBottom": "20px"}),

        html.Div(id="tables-container", style={
            "display": "flex",
            "flexWrap": "wrap",
            "justifyContent": "center",
            "gap": "20px"
        }),

        html.Div(id="copy-output", style={
            "textAlign": "center",
            "marginTop": "10px",
            "color": "green"
        })
    ])
