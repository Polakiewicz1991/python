from dash import Input, Output, State, ctx, no_update
import plotly.graph_objs as go
import os
import glob

from Flatness.Web.data_handler import parse_csv
from Flatness.Web.flatness_calculator import calculate_flatness
from Flatness.Web.plot3d import create_3d_scatter, create_3d_scatter_no_bar
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

DEFAULT_FOLDER_PATH = r"E:\PP\23_0005_0000 - Portal pomiarowy do stołów\Dokumentacja"


def register_callbacks(app):
    # @app.callback(
    #     Output('interval-update', 'interval'),
    #     Input('refresh-interval', 'value')
    # )
    # def update_refresh_interval(seconds):
    #     return seconds * 1000  # sekundy → ms

    @app.callback(
        Output('current-folder-label', 'children'),
        Input('select-folder-btn', 'n_clicks'),
        State('folder-input', 'value'),
        prevent_initial_call=True
    )
    def select_folder(n_clicks, folder_input):
        return folder_input

    @app.callback(
        Output('interval-update', 'disabled'),
        Output('interval-update', 'interval'),
        Output('interval-toggle-btn', 'children'),
        Input('interval-toggle-btn', 'n_clicks'),
        Input('refresh-interval', 'value'),
        State('interval-update', 'disabled'),
        prevent_initial_call=True
    )
    def toggle_interval(n_clicks, refresh_value, disabled):
        interval_ms = refresh_value * 1000 if refresh_value else 30_000
        if disabled:
            # Start
            return False, interval_ms, "Stop"
        else:
            # Stop
            return True, interval_ms, "Start"


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
        Input('language-selector', 'value'),  # 🟡 DODANE
        State('chart_plate', 'figure'),
        State('chart_side_Y1', 'figure'),
        State('tabs', 'value'),
        prevent_initial_call=True
    )
    def update_or_reset(contents, n_clicks, n_intervals, lang, chart_plate, current_fig2, current_tab):
        tr = translations.get(lang, translations['pl'])

        # Callback działa TYLKO gdy aktywna jest zakładka wykresów
        if current_tab != 'tab-wykresy':
            return no_update, no_update, no_update, no_update, no_update, no_update

        triggered_id = ctx.triggered_id if hasattr(ctx, "triggered_id") else None

        # --- 1️⃣ Wywołanie przez upload ---
        if triggered_id == 'upload-data':
            if contents is None:
                empty_fig = go.Figure()
                empty_fig.update_layout(title=tr['upload_csv'])
                return empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, ""
            try:
                df = parse_csv(contents)
            except Exception as e:
                empty_fig = go.Figure()
                empty_fig.update_layout(title=f"{tr['file_load_error']}: {str(e)}")
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
                empty_fig.update_layout(title=tr['no_csv_files'])
                return empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, ""

            # Wybierz najnowszy plik po dacie modyfikacji
            latest_file = max(csv_files, key=os.path.getmtime)

            try:
                df = parse_csv(latest_file)  # parse_csv obsługuje teraz również lokalną ścieżkę
            except Exception as e:
                empty_fig = go.Figure()
                empty_fig.update_layout(title=f"{tr['file_load_error']}: {str(e)}")
                return empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, ""

        # --- 4️⃣ Zmiana języka bez danych ---
        else:
            if 'df' not in locals():
                empty_fig = go.Figure()
                empty_fig.update_layout(title=tr['no_data'])
                return empty_fig, empty_fig, empty_fig, empty_fig, empty_fig, ""

        # --- Generowanie wykresów i wartości płaskości ---
        flatness_value, coeffs, deviations = calculate_flatness(df)

        fig_main = create_3d_scatter(df, coeffs, deviations, lang=lang, view='main')
        fig_sideX1 = create_3d_scatter_no_bar(df, coeffs, deviations, lang=lang, view='side_x1')
        fig_sideY1 = create_3d_scatter_no_bar(df, coeffs, deviations, lang=lang, view='side_y1')
        fig_sideX2 = create_3d_scatter_no_bar(df, coeffs, deviations, lang=lang, view='side_x2')
        fig_sideY2 = create_3d_scatter_no_bar(df, coeffs, deviations, lang=lang, view='side_y2')

        fig_main.update_layout(scene_camera=default_camera)
        fig_sideX1.update_layout(scene_camera=default_camera2)
        fig_sideY1.update_layout(scene_camera=default_camera2)
        fig_sideX2.update_layout(scene_camera=default_camera2)
        fig_sideY2.update_layout(scene_camera=default_camera2)

        flatness_text = f"{tr['flatness_value']}: {flatness_value:.4f}"

        return fig_main, fig_sideX1, fig_sideY1, fig_sideX2, fig_sideY2, flatness_text
