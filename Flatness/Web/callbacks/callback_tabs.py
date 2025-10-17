from dash import Input, Output, State, ctx, no_update
from Flatness.Web.layouts.layout_plots import get_3d_plots_layout
from Flatness.Web.layouts.layout_plc import  get_plc_layout

def register_callbacks(app):

    # Callback do zmiany zakładek i renderowania ich zawartości
    @app.callback(
        Output('tabs-content', 'children'),
        Input('tabs', 'value'),
        Input('language-selector', 'value')
    )
    def render_tab_content(tab, lang):
        if tab == 'tab-wykresy':
            return get_3d_plots_layout(lang=lang)  # jeśli get_3d_plots_layout obsługuje język
        elif tab == 'tab-plc':
            return get_plc_layout(lang=lang)
        return "Nieznana zakładka"