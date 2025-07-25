from dash import Input, Output, State, ctx, no_update
import plotly.graph_objs as go

import time
import threading
import pyads

def register_callbacks(app):
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