from dash import Input, Output, dcc
from Flatness.Web.layouts.layout_plots import get_3d_plots_layout
from Flatness.Web.layouts.layout_plc import get_plc_layout
from Flatness.Web.layouts.translations import translations

def register_callbacks(app):

    # --- 1️⃣ Dynamiczne tłumaczenie zakładek ---
    @app.callback(
        Output('tabs-container', 'children'),
        Input('language-selector', 'value')
    )
    def update_tabs(lang):
        tr = translations.get(lang, translations['pl'])
        return dcc.Tabs(
            id='tabs',
            value='tab-wykresy',
            children=[
                dcc.Tab(label=tr['tab_wykresy'], value='tab-wykresy'),
                dcc.Tab(label=tr['tab_plc'], value='tab-plc'),
            ],
            style={'flexGrow': '1'}
        )

    # --- 2️⃣ Zawartość zakładek w wybranym języku ---
    @app.callback(
        Output('tabs-content', 'children'),
        Input('tabs', 'value'),
        Input('language-selector', 'value'),
        #prevent_initial_call=True
    )
    def render_tab_content(tab, lang):
        if tab == 'tab-wykresy':
            return get_3d_plots_layout(lang=lang)
        elif tab == 'tab-plc':
            return get_plc_layout(lang=lang)
        return "Nieznana zakładka"