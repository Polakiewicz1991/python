from dash import Input, Output, State, ctx, no_update
import plotly.graph_objs as go

import pyads

from data_handler import parse_csv
from flatness_calculator import calculate_flatness
from plot3d import create_3d_scatter, create_3d_scatter_top

from layout import get_3d_plots_layout, get_plc_data_layout, get_plc_layout

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

    # Callback do zmiany zakładek i renderowania ich zawartości
    @app.callback(
        Output('tabs-content', 'children'),
        Input('tabs', 'value')
    )
    def render_tab_content(tab):
        if tab == 'tab-wykresy':
            return get_3d_plots_layout()
        elif tab == 'tab-plc':
            return get_plc_layout()
        return "Nieznana zakładka"

    # Callback do aktualizacji wykresów (dane 3D) - działa tylko gdy aktywna jest zakładka wykresów
    @app.callback(
        Output('three-d-plot-1', 'figure'),
        Output('three-d-plot-2', 'figure'),
        Output('three-d-plot-3', 'figure'),
        Output('flatness-output', 'children'),
        Input('upload-data', 'contents'),
        Input('reset-view-btn', 'n_clicks'),
        State('three-d-plot-1', 'figure'),
        State('three-d-plot-3', 'figure'),
        State('tabs', 'value'),
        prevent_initial_call=True
    )
    def update_or_reset(contents, n_clicks, current_fig, current_fig2, current_tab):
        # Callback działa TYLKO gdy aktywna jest zakładka z wykresami
        if current_tab != 'tab-wykresy':
            return no_update, no_update, no_update, no_update

        triggered_id = ctx.triggered_id if hasattr(ctx, "triggered_id") else None

        if triggered_id == 'upload-data':
            if contents is None:
                empty_fig = go.Figure()
                empty_fig.update_layout(title='Wczytaj plik CSV, aby wyświetlić wykres')
                return empty_fig, empty_fig, empty_fig, ""
            try:
                df = parse_csv(contents)
            except Exception as e:
                empty_fig = go.Figure()
                empty_fig.update_layout(title=f"Błąd wczytywania pliku: {str(e)}")
                return empty_fig, empty_fig, empty_fig, ""

            flatness_value, coeffs, deviations = calculate_flatness(df)
            fig_new = create_3d_scatter(df, coeffs, deviations)
            fig_new2 = create_3d_scatter_top(df, coeffs, deviations)
            fig_new.update_layout(scene_camera=default_camera)
            fig_new2.update_layout(scene_camera=default_camera2)
            flatness_text = f"Płaskość powierzchni (metodą najmniejszych kwadratów): {flatness_value:.4f}"
            return fig_new, fig_new, fig_new2, flatness_text

        elif triggered_id == 'reset-view-btn' and current_fig is not None and current_fig2 is not None:
            current_fig['layout']['scene']['camera'] = default_camera
            current_fig2['layout']['scene']['camera'] = default_camera2
            return current_fig, current_fig, current_fig2, no_update

        empty_fig = go.Figure()
        empty_fig.update_layout(title='Wczytaj plik CSV, aby wyświetlić wykres')
        return empty_fig, empty_fig, empty_fig, ""

    PLC_AMS_ID = '5.103.232.148.1.1'
    PLC_PORT = pyads.PORT_TC3PLC1

    @app.callback(
        Output('val-sReferenceActive', 'children'),
        Output('val-sReferenceNextToActive', 'children'),
        Output('val-bBlinker_1000ms', 'children'),
        Input('interval-plc', 'n_intervals')
    )
    def update_plc_values(n):
        try:
            with pyads.Connection(PLC_AMS_ID, PLC_PORT) as plc:
                val_sRefActive = plc.read_by_name('GVL_Reference.sReferenceActive', pyads.PLCTYPE_STRING)
                val_sRefNextToActive = plc.read_by_name('GVL_Reference.sReferenceNextToActive', pyads.PLCTYPE_STRING)
                val_bool = plc.read_by_name('MAIN.bBlinker_1000ms', pyads.PLCTYPE_BOOL)
                print(f"{val_sRefActive}, {val_sRefNextToActive}, str({val_bool})")
            return val_sRefActive, val_sRefNextToActive, str(val_bool)
        except Exception as e:
            err_msg = f"Błąd: {str(e)}"
            return err_msg, err_msg, err_msg