from dash import Input, Output, dcc, html
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

        base_tab_style = {
            'padding': '12px 32px',
            'fontWeight': '600',
            'fontSize': '16px',
            'borderRadius': '10px 10px 0 0',
            'backgroundColor': '#f7f7f7',
            'color': '#333',
            'border': '1px solid #ddd',
            'marginRight': '4px',
            'height': '60px',                # 🔹 stała wysokość zakładki
            'display': 'flex',               # 🔹 wyśrodkowanie w pionie
            'alignItems': 'center',
            'justifyContent': 'center',
            'boxSizing': 'border-box',
            'minWidth': '160px',             # 🔹 równa szerokość minimalna
            'cursor': 'pointer',
            'transition': 'background-color 0.2s ease',
        }

        selected_tab_style = {
            **base_tab_style,
            'backgroundColor': '#ffffff',
            'border': '1px solid #ccc',
            'borderBottom': 'none',
            'color': '#1890ff',
            'boxShadow': '0 -2px 6px rgba(0,0,0,0.05)',
            'fontWeight': '700',
        }

        return html.Div([
            dcc.Tabs(
                id='tabs',
                value='tab-wykresy',
                children=[
                    dcc.Tab(label=tr['tab_wykresy'], value='tab-wykresy',
                            style=base_tab_style, selected_style=selected_tab_style),
                    dcc.Tab(label=tr['tab_plc'], value='tab-plc',
                            style=base_tab_style, selected_style=selected_tab_style),
                ],
                style={
                    'display': 'flex',
                    'flexDirection': 'row',
                    'alignItems': 'center',
                    'justifyContent': 'center',
                    'backgroundColor': '#fafafa',
                    'borderBottom': '1px solid #ddd',
                    'paddingTop': '10px',
                    'gap': '4px',
                },
            ),
        ], style={
            'width': '100%',
            'backgroundColor': '#fafafa',
            'borderRadius': '12px 12px 0 0',
            'boxShadow': '0 2px 6px rgba(0,0,0,0.08)',
            'marginBottom': '10px',
        })


    # --- 2️⃣ Zawartość zakładek ---
    @app.callback(
        Output('tabs-content', 'children'),
        Input('tabs', 'value'),
        Input('language-selector', 'value'),
    )
    def render_tab_content(tab, lang):
        tr = translations.get(lang, translations['pl'])
        content_style = {
            'padding': '20px 30px',
            'backgroundColor': '#ffffff',
            'borderRadius': '0 0 12px 12px',
            'boxShadow': '0 2px 8px rgba(0,0,0,0.05)',
            'minHeight': '700px',
        }

        if tab == 'tab-wykresy':
            return html.Div(get_3d_plots_layout(lang=lang), style=content_style)
        elif tab == 'tab-plc':
            return html.Div(get_plc_layout(lang=lang), style=content_style)
        else:
            return html.Div(tr['unknown_tab'], style=content_style)