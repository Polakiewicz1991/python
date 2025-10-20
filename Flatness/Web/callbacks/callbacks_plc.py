from dash import Input, Output, State, ctx, no_update

import time
import threading
import pyads

def register_callbacks(app):
    #PLC_AMS_ID = '192.168.1.50.1.1'
    PLC_AMS_ID = '192.168.1.254.1.1'
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
        #Output('val-bBlinker_1000ms', 'children'),
        *[Output(f'val-sReferenceNames_{i}', 'children') for i in range(14)],
        Output('val_CONTROLiReferenceShow', 'data'),
        Output('val_MAPsName', 'children'),
        Output('val_MAPstTableParamiSYSTEM', 'children'),
        Output('val_MAPstTableParamrDIMENSION_X', 'children'),
        Output('val_MAPstTableParamrDIMENSION_Y', 'children'),
        Output('val_MAPstTableParamrDIMENSION_Z', 'children'),
        Input('interval-plc', 'n_intervals')
    )
    def update_plc_values(n):
        val_sReferenceNames = []
        try:
            with pyads.Connection(PLC_AMS_ID, PLC_PORT) as plc:
                val_sRefActive = plc.read_by_name('GVL_Reference.sReferenceActive', pyads.PLCTYPE_STRING)
                val_sRefNextToActive = plc.read_by_name('GVL_Reference.sReferenceNextToActive', pyads.PLCTYPE_STRING)
                val_CONTROLiReferenceShow = plc.read_by_name('GVL_Reference.CONTROL.iReferenceShow', pyads.PLCTYPE_INT)
                val_MAPsName = plc.read_by_name('GVL_Reference.MAP.sName', pyads.PLCTYPE_STRING)
                val_MAPstTableParamiSYSTEM = plc.read_by_name('GVL_Reference.MAP.stTableParam.iSYSTEM',
                                                                   pyads.PLCTYPE_INT)
                val_MAPstTableParamrDIMENSION_X = plc.read_by_name('GVL_Reference.MAP.stTableParam.rDIMENSION_X',
                                                                   pyads.PLCTYPE_REAL)
                val_MAPstTableParamrDIMENSION_Y = plc.read_by_name('GVL_Reference.MAP.stTableParam.rDIMENSION_Y',
                                                                   pyads.PLCTYPE_REAL)
                val_MAPstTableParamrDIMENSION_Z = plc.read_by_name('GVL_Reference.MAP.stTableParam.rDIMENSION_Z',
                                                                   pyads.PLCTYPE_REAL)

                #val_bool = plc.read_by_name('MAIN.bBlinker_1000ms', pyads.PLCTYPE_BOOL)
                print(f"{val_sRefActive}, {val_sRefNextToActive}") #, str({val_bool})")

                for i in range(14):  # 0 do 13
                    var_name = f'GVL_Reference.sReferenceNames[{i}]'
                    val = plc.read_by_name(var_name, pyads.PLCTYPE_STRING)
                    val_sReferenceNames.append(val or '')

                print("val_sReferenceNames: ", val_sReferenceNames)
                print("val_CONTROLiReferenceShow: ",val_CONTROLiReferenceShow)

            return (val_sRefActive, val_sRefNextToActive, *val_sReferenceNames, val_CONTROLiReferenceShow, val_MAPsName,
                    val_MAPstTableParamiSYSTEM, val_MAPstTableParamrDIMENSION_X, val_MAPstTableParamrDIMENSION_Y, val_MAPstTableParamrDIMENSION_Z)
        except Exception as e:
            import traceback
            print("Błąd w update_plc_values:", str(e))
            traceback.print_exc()
            err_msg = f"Błąd: {str(e)}"
            return (err_msg,) * 22

    # liczba wierszy w tabeli
    ROW_COUNT = 14

    @app.callback(
        [Output(f'reference_row_{i}', 'style') for i in range(ROW_COUNT)],
        Input('val_CONTROLiReferenceShow', 'data')
    )
    def highlight_active_row(active_index):
        # styl podstawowy (wszystkie wiersze)
        base_style = {
            'padding': '8px 12px',
            'fontSize': '16px',
            'borderBottom': '1px solid #eee',
            'height': '40px',
            'backgroundColor': 'white'
        }

        # styl aktywnego wiersza
        active_style = {
            **base_style,
            'backgroundColor': '#e6f7ff',  # delikatny niebieski
            'borderLeft': '4px solid #1890ff',
            'fontWeight': '600',
        }

        styles = []
        for i in range(ROW_COUNT):
            if active_index == i:
                styles.append(active_style)
            else:
                styles.append(base_style)
        return styles

    @app.callback(
        Output('btn-CONTROLbActive', 'n_clicks'),  # resetujemy kliknięcia, by można było ponownie kliknąć
        Input('btn-CONTROLbActive', 'n_clicks'),
        prevent_initial_call=True
    )
    def handle_btn_bRefActive(n_clicks):
        if n_clicks:
            threading.Thread(target=momentary_write, args=('GVL_Reference.CONTROL.bActivate',), daemon=True).start()
        return 0  # reset clicks

    @app.callback(
        Output('btn-CONTROLbDisplayUp', 'n_clicks'),  # resetujemy kliknięcia, by można było ponownie kliknąć
        Input('btn-CONTROLbDisplayUp', 'n_clicks'),
        prevent_initial_call=True
    )
    def handle_btn_bDisplayUp(n_clicks):
        if n_clicks:
            threading.Thread(target=momentary_write, args=('GVL_Reference.CONTROL.bDisplayUp',), daemon=True).start()
        return 0  # reset clicks

    @app.callback(
        Output('btn-CONTROLbDisplayDown', 'n_clicks'),  # resetujemy kliknięcia, by można było ponownie kliknąć
        Input('btn-CONTROLbDisplayDown', 'n_clicks'),
        prevent_initial_call=True
    )
    def handle_btn_bDisplayDown(n_clicks):
        if n_clicks:
            threading.Thread(target=momentary_write, args=('GVL_Reference.CONTROL.bDisplayDown',), daemon=True).start()
        return 0  # reset clicks