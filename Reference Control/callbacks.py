from dash import Output, Input, State, html, dash_table, ctx, no_update
from data_utils import flatten_dict
import pandas as pd
import numpy as np
import json


def safe_value(value):
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    elif isinstance(value, (np.generic,)):
        return value.item()
    elif value is None:
        return ""
    else:
        return value


def register_callbacks(app, all_data):

    # --- GENERATOR TABELI ---
    @app.callback(
        Output("tables-container", "children"),
        Input("file-multi-dropdown", "value")
    )
    def update_tables(selected_files):
        if not selected_files:
            return html.P("Select one or more CSV files to view.",
                          style={"color": "gray", "textAlign": "center"})

        base_filename = selected_files[0]
        base_data = all_data.get(base_filename, {})
        base_flat = flatten_dict(base_data)
        df = pd.DataFrame(list(base_flat.items()), columns=["Variable", base_filename])

        for filename in selected_files[1:]:
            flat = flatten_dict(all_data.get(filename, {}))
            df_temp = pd.DataFrame(list(flat.items()), columns=["Variable", filename])
            df = pd.merge(df, df_temp, on="Variable", how="outer")

        df = df.fillna("")
        df = df.map(safe_value)

        df.insert(0, "Overwrite?", ["⬜"] * len(df))

        style_data_conditional = []
        if len(selected_files) > 1:
            ref_col = base_filename
            for col in selected_files[1:]:
                style_data_conditional.append({
                    "if": {"filter_query": f"{{{col}}} != {{{ref_col}}}", "column_id": col},
                    "backgroundColor": "#ffcccc"
                })

        columns = (
            [{"name": "Overwrite?", "id": "Overwrite?", "presentation": "markdown"}] +
            [{"name": "Variable", "id": "Variable"}] +
            [{"name": col, "id": col} for col in selected_files]
        )

        table = dash_table.DataTable(
            id="comparison-table",
            columns=columns,
            data=df.to_dict("records"),
            row_selectable="multi",
            editable=True,
            style_table={"overflowY": "visible", "maxHeight": "none"},
            style_cell={
                "textAlign": "left",
                "padding": "6px",
                "whiteSpace": "pre-wrap",
                "fontFamily": "monospace",
                "fontSize": "13px",
            },
            style_header={
                "backgroundColor": "#f2f2f2",
                "fontWeight": "bold",
                "textAlign": "center"
            },
            style_data_conditional=style_data_conditional,
            page_action="none",
        )

        return html.Div([
            html.H3(f"Comparison based on: {base_filename}",
                    style={"textAlign": "center", "marginBottom": "15px"}),
            table
        ], style={
            "flex": "1 0 100%",
            "minWidth": "90%",
            "border": "1px solid #ccc",
            "borderRadius": "10px",
            "padding": "10px",
            "backgroundColor": "#fff",
            "boxShadow": "0 2px 6px rgba(0,0,0,0.1)"
        })

    # --- KOPIOWANIE WARTOŚCI Z TABELI 1 DO POZOSTAŁYCH ---
    @app.callback(
        Output("comparison-table", "data"),
        Output("copy-output", "children"),
        Input("copy-button", "n_clicks"),
        State("comparison-table", "derived_virtual_selected_rows"),
        State("comparison-table", "data"),
        State("file-multi-dropdown", "value"),
        prevent_initial_call=True
    )
    def copy_values_between_files(n_clicks, selected_rows, table_data, selected_files):
        if not selected_rows or not table_data or len(selected_files) < 2:
            return table_data, "⚠️ No rows or target files selected."

        base_col = selected_files[0]
        target_cols = selected_files[1:]

        # kopiujemy wartości
        for i in selected_rows:
            base_value = table_data[i][base_col]
            for col in target_cols:
                table_data[i][col] = base_value

        return table_data, f"✅ Copied {len(selected_rows)} rows from '{base_col}' to {len(target_cols)} table(s)."
