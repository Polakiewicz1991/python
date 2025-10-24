from dash import html, dcc, dash_table

def create_layout(file_list):
    return html.Div([
        html.H1("CSV Data Viewer", className="text-2xl font-bold mb-4"),

        html.Div([
            html.Label("Select CSV file:", className="font-semibold"),
            dcc.Dropdown(
                id="file-dropdown",
                options=[{"label": f, "value": f} for f in file_list],
                placeholder="Choose a CSV file",
                style={"width": "400px"}
            )
        ], className="mb-4"),

        html.Div(id="table-container"),
    ], style={"padding": "20px"})
