from dash import Input, Output, State, ctx, no_update
import plotly.graph_objs as go
import os
import glob

from Flatness.Web.data_handler import parse_csv
from Flatness.Web.flatness_calculator import calculate_flatness
from Flatness.Web.plot3d import create_3d_scatter, create_3d_scatter_top
from Flatness.Web.layouts.translations import translations

from Flatness.Web.layouts.layout_plots import get_3d_plots_layout

default_camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=1.25, y=2, z=1.25)
)
default_camera2 = dict(
    up=dict(x=0, y=0, z=2),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=1, y=0, z=3)
)

def register_callbacks(app):
    @app.callback(
        Output('chart_plate', 'figure'),
        Output('chart_side_X1', 'figure'),
        Output('chart_side_Y1', 'figure'),
        Output('chart_side_X2', 'figure'),
        Output('chart_side_Y2', 'figure'),
        Output('flatness-output', 'children'),
        Input('upload-data', 'contents'),
        Input('reset-view-btn', 'n_clicks'),
        Input('interval-update', 'n_intervals'),  # ← dodany automatyczny interwał
        State('chart_plate', 'figure'),
        State('chart_side_Y1', 'figure'),
        State('tabs', 'value'),
        prevent_initial_call=True
    )
    def update_or_reset(contents, n_clicks, n_intervals, chart_plate, current_fig2, current_tab):
        # Callback działa TYLKO gdy aktywna jest zakładka wykresów
        if current_tab != 'tab-wykresy':
            return no_update, no_update, no_update, no_update, no_update, no_update

        triggered_id = ctx.triggered_id if hasattr(ctx, "triggered_id") else None

        # --- 1️⃣ Wywołanie przez upload ---
        if triggered_id == 'upload-data':
            if contents is None:
                empty_fig = go.Figure()
                empty_fig.update_layout(title='Wczytaj plik CSV, aby wyświetlić wykres')
                return empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, ""
            try:
                df = parse_csv(contents)
            except Exception as e:
                empty_fig = go.Figure()
                empty_fig.update_layout(title=f"Błąd wczytywania pliku: {str(e)}")
                return empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, ""

        # --- 2️⃣ Wywołanie przez reset ---
        elif triggered_id == 'reset-view-btn' and chart_plate is not None and current_fig2 is not None:
            chart_plate['layout']['scene']['camera'] = default_camera
            current_fig2['layout']['scene']['camera'] = default_camera2
            return chart_plate, chart_plate, chart_plate, chart_plate, current_fig2, no_update

        # --- 3️⃣ Wywołanie przez Interval (automatyczne) ---
        elif triggered_id == 'interval-update':
            # Ścieżka do folderu z CSV
            folder_path = r"E:\PP\23_0005_0000 - Portal pomiarowy do stołów\Dokumentacja"

            # Znajdź wszystkie pliki CSV w folderze
            csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

            if not csv_files:
                empty_fig = go.Figure()
                empty_fig.update_layout(title="Brak plików CSV w folderze")
                return empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, ""

            # Wybierz najnowszy plik po dacie modyfikacji
            latest_file = max(csv_files, key=os.path.getmtime)

            try:
                df = parse_csv(latest_file)  # parse_csv obsługuje teraz również lokalną ścieżkę
            except Exception as e:
                empty_fig = go.Figure()
                empty_fig.update_layout(title=f"Błąd wczytywania pliku: {str(e)}")
                return empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, ""

        # --- Generowanie wykresów i wartości płaskości ---
        flatness_value, coeffs, deviations = calculate_flatness(df)
        fig_new = create_3d_scatter(df, coeffs, deviations)
        fig_new2 = create_3d_scatter_top(df, coeffs, deviations)
        fig_new.update_layout(scene_camera=default_camera)
        fig_new2.update_layout(scene_camera=default_camera2)
        flatness_text = f"Płaskość powierzchni (metodą najmniejszych kwadratów): {flatness_value:.4f}"

        return fig_new, fig_new, fig_new, fig_new, fig_new2, flatness_text
