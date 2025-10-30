# callbacks.py
from dash import Output, Input, State, html, dash_table
from data_utils import flatten_dict, save_dict_to_csv
import pandas as pd
import json
import os

FOLDER_PATH = "./csv_data"

def safe_value(value):
    # convert complex values to JSON string for table display
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    if value is None:
        return ""
    return value

def register_callbacks(app, all_data):

    # ---------- 1) GENEROWANIE TABELI ----------
    @app.callback(
        Output("tables-container", "children"),
        Input("file-multi-dropdown", "value"),
        prevent_initial_call=True
    )
    def update_tables(selected_files):
        if not selected_files:
            return html.P("Select one or more CSV files to view.",
                          style={"color": "gray", "textAlign": "center"})

        # build comparison dataframe
        base_filename = selected_files[0]
        base_flat = flatten_dict(all_data.get(base_filename, {}))
        df = pd.DataFrame(list(base_flat.items()), columns=["Variable", base_filename])

        for filename in selected_files[1:]:
            flat = flatten_dict(all_data.get(filename, {}))
            df_temp = pd.DataFrame(list(flat.items()), columns=["Variable", filename])
            df = pd.merge(df, df_temp, on="Variable", how="outer")

        df = df.fillna("")
        df = df.applymap(safe_value)

        # Use row_selectable to select rows — simpler and robust
        columns = [{"name": "Variable", "id": "Variable"}] + [{"name": col, "id": col} for col in selected_files]

        table = dash_table.DataTable(
            id="comparison-table",
            columns=columns,
            data=df.to_dict("records"),
            row_selectable="multi",    # user can select rows (works reliably)
            selected_rows=[],          # ensure property exists
            editable=True,             # allow editing cells if needed
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
            page_action="none"
        )

        return html.Div([
            html.H3(f"Comparison based on: {base_filename}",
                    style={"textAlign": "center", "marginBottom": "12px"}),
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


    # ---------- 2) COPY SELECTED: kopiuj wartości z kolumny 0 do innych kolumn ----------
    @app.callback(
        Output("comparison-table", "data"),
        Output("copy-output", "children"),
        Input("copy-button", "n_clicks"),
        State("comparison-table", "selected_rows"),
        State("comparison-table", "data"),
        State("file-multi-dropdown", "value"),
        prevent_initial_call=True
    )
    def copy_selected_to_targets(n_clicks, selected_rows, table_data, selected_files):
        # safety guards
        if not table_data:
            return dash_table.DataTable().data, "⚠️ Table empty."
        if not selected_files or len(selected_files) < 2:
            return table_data, "⚠️ Select at least 2 files (one source + targets)."
        if not selected_rows:
            return table_data, "⚠️ No rows selected."

        base_col = selected_files[0]
        target_cols = selected_files[1:]

        # Work on a copy to avoid mutation surprises
        new_data = [row.copy() for row in table_data]

        for r_idx in selected_rows:
            # guard row index range
            if r_idx < 0 or r_idx >= len(new_data):
                continue
            base_value = new_data[r_idx].get(base_col, "")
            # copy into every target column
            for tcol in target_cols:
                new_data[r_idx][tcol] = base_value

        return new_data, f"✅ Copied {len(selected_rows)} row(s) from '{base_col}' to {len(target_cols)} target file(s)."


    # ---------- 3) SAVE CHANGES: zapisz bieżące dane tabeli do CSV ----------
    @app.callback(
        Output("copy-output", "children", allow_duplicate=True),
        Input("save-button", "n_clicks"),
        State("comparison-table", "data"),
        State("file-multi-dropdown", "value"),
        prevent_initial_call=True
    )
    def save_table_to_csv(n_clicks, table_data, selected_files):
        if not table_data:
            return "⚠️ No data to save."
        if not selected_files:
            return "⚠️ No files selected."

        try:
            # rebuild per-file dictionaries and save
            for filename in selected_files:
                new_dict = {}
                for row in table_data:
                    var = row.get("Variable")
                    if var is None:
                        continue
                    # read value for this filename (if missing -> empty string)
                    value = row.get(filename, "")
                    new_dict[var] = value
                file_path = os.path.join(FOLDER_PATH, filename)
                save_dict_to_csv(new_dict, file_path)

            return f"✅ Saved changes to {len(selected_files)} file(s)."
        except Exception as e:
            return f"❌ Error saving: {e}"
