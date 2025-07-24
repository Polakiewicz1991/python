from dash import Input, Output, State, ctx, no_update
import plotly.graph_objs as go

import time
import threading
import pyads

from data_handler import parse_csv
from flatness_calculator import calculate_flatness
from plot3d import create_3d_scatter, create_3d_scatter_top

from layout import get_3d_plots_layout, get_plc_layout

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

    def momentary_write(plc_var):
        print("plc_var: ", plc_var)
        try:
            with pyads.Connection(PLC_AMS_ID, PLC_PORT) as plc:
                plc.write_by_name(plc_var, True, pyads.PLCTYPE_BOOL)
                time.sleep(0.3)  # 300 ms przytrzymania
                plc.write_by_name(plc_var, False, pyads.PLCTYPE_BOOL)
        except Exception as e:
            print("Błąd momentary_write:", e)

    @app.callback(
        Output('val-sReferenceActive', 'children'),
        Output('val-sReferenceNextToActive', 'children'),
        Output('val-bBlinker_1000ms', 'children'),
        *[Output(f'val-sReferenceNames_{i}', 'children') for i in range(14)],
        Output('val_CONTROLiSelectedRef', 'data'),
        Input('interval-plc', 'n_intervals')
    )
    def update_plc_values(n):
        val_sReferenceNames = []
        try:
            with pyads.Connection(PLC_AMS_ID, PLC_PORT) as plc:
                val_sRefActive = plc.read_by_name('GVL_Reference.sReferenceActive', pyads.PLCTYPE_STRING)
                val_sRefNextToActive = plc.read_by_name('GVL_Reference.sReferenceNextToActive', pyads.PLCTYPE_STRING)
                val_CONTROLiSelectedRef = plc.read_by_name('GVL_Reference.CONTROL.iSelectedRef', pyads.PLCTYPE_INT)
                val_bool = plc.read_by_name('MAIN.bBlinker_1000ms', pyads.PLCTYPE_BOOL)
                print(f"{val_sRefActive}, {val_sRefNextToActive}, str({val_bool})")

                for i in range(14):  # 0 do 13
                    var_name = f'GVL_Reference.sReferenceNames[{i}]'
                    val = plc.read_by_name(var_name, pyads.PLCTYPE_STRING)
                    val_sReferenceNames.append(val or '')

                print("val_sReferenceNames: ", val_sReferenceNames)
                print("val_CONTROLiSelectedRef: ",val_CONTROLiSelectedRef)

            return val_sRefActive, val_sRefNextToActive, str(val_bool), *val_sReferenceNames, val_CONTROLiSelectedRef
        except Exception as e:
            import traceback
            print("Błąd w update_plc_values:", str(e))
            traceback.print_exc()
            err_msg = f"Błąd: {str(e)}"
            return (err_msg,) * 18

    @app.callback(
        [Output(f'row_{i}', 'style') for i in range(14)],
        Input('val_CONTROLiSelectedRef', 'data')
    )
    def highlight_selected_row(selected_index):
        style_default = {}
        style_highlight = {
            'backgroundColor': '#d0f0c0',
            'border': '2px solid green',
            'borderRadius': '4px'
        }

        styles = []
        for i in range(14):
            if i == selected_index:
                styles.append(style_highlight)
            else:
                styles.append(style_default)
        return styles

    @app.callback(
        Output('btn-CONTROLbActive', 'n_clicks'),  # resetujemy kliknięcia, by można było ponownie kliknąć
        Input('btn-CONTROLbActive', 'n_clicks'),
        prevent_initial_call=True
    )
    def handle_btn_srefactive(n_clicks):
        if n_clicks:
            threading.Thread(target=momentary_write, args=('GVL_Reference.CONTROL.bActivate',), daemon=True).start()
        return 0  # reset clicks