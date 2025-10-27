from dash import html, dcc

def serve_layout(all_data):
    return html.Div([

        # --- 🔹 Pasek nawigacyjny (sticky header) ---
        html.Div([
            html.H2("CSV Comparison Tool", style={
                "color": "white",
                "margin": "0",
                "padding": "0 20px",
                "flex": "1"
            }),

            dcc.Dropdown(
                id="file-multi-dropdown",
                options=[{"label": f, "value": f} for f in all_data.keys()],
                multi=True,
                placeholder="Select CSV files to compare...",
                style={
                    "width": "50%",
                    "display": "inline-block",
                    "marginRight": "10px",
                    "verticalAlign": "middle",
                }
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
                    "cursor": "pointer"
                },
            ),

            html.Div(id="copy-output", style={
                "marginLeft": "20px",
                "color": "#d4edda",
                "fontWeight": "bold",
                "flex": "0.5"
            }),
        ],
            id="navbar",
            style={
                "position": "fixed",       # <- zawsze na górze
                "top": "0",
                "left": "0",
                "right": "0",
                "height": "60px",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "space-between",
                "backgroundColor": "#343a40",
                "boxShadow": "0 2px 6px rgba(0,0,0,0.2)",
                "padding": "0 10px",
                "zIndex": "1000"
            }
        ),

        # --- 🔹 Główna sekcja (tabele) ---
        html.Div(
            id="tables-container",
            style={
                "display": "flex",
                "flexWrap": "wrap",
                "justifyContent": "center",
                "gap": "20px",
                "paddingTop": "80px",  # <- odsuń zawartość, żeby pasek nie zasłaniał
                "paddingBottom": "40px"
            }
        )
    ],
        style={
            "backgroundColor": "#f8f9fa",
            "minHeight": "100vh"
        }
    )
