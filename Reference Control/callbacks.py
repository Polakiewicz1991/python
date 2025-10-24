from dash import Output, Input, dash_table, html
from data_utils import flatten_dict
import json

def register_callbacks(app, all_data):
    @app.callback(
        Output("table-container", "children"),
        Input("file-dropdown", "value")
    )
    def update_table(selected_file):
        if not selected_file:
            return html.P("Please select a CSV file.", style={"color": "gray"})

        data = all_data[selected_file]
        flat_data = flatten_dict(data)

        # ✅ Convert complex types (list/dict) to string for display
        table_data = []
        for k, v in flat_data.items():
            if isinstance(v, (list, dict)):
                v = json.dumps(v, ensure_ascii=False)  # czytelny zapis np. [[1,0],[0,1]]
            table_data.append({"variable": k, "value": v})

        table = dash_table.DataTable(
            columns=[
                {"name": "Variable", "id": "variable"},
                {"name": "Value", "id": "value"}
            ],
            data=table_data,
            style_table={"overflowX": "auto"},
            style_cell={
                "textAlign": "left",
                "padding": "6px",
                "whiteSpace": "pre-wrap",
                "fontFamily": "monospace",
                "fontSize": "14px"
            },
            style_header={
                "backgroundColor": "#f2f2f2",
                "fontWeight": "bold"
            },
            page_size=20
        )

        return html.Div([
            html.H3(selected_file, style={"marginBottom": "10px"}),
            table
        ])
