from dash import html
from Flatness.Web.layouts.translations import translations

def get_buttons(lang='pl'):
    tr = translations.get(lang, translations['pl'])

    def make_button(icon_src, text, button_id):
        return html.Button([
            html.Img(
                src=f"../assets/{icon_src}",
                alt="icon",
                style={'width': '100px', 'height': '100px', 'padding': '5px', 'marginRight': '2px'}
            ),
            html.Span(
                text,
                style={
                    'display': 'inline-block',
                    'transform': 'rotate(270deg)',
                    'transformOrigin': 'center center',
                    'whiteSpace': 'pre-line',
                    'textAlign': 'center',
                    'lineHeight': 'normal',
                    'fontSize': '25px'
                }
            )
        ], style={'display': 'flex', 'alignItems': 'center'}, id=button_id)

    button_with_process_icon = make_button("processColor.svg", tr['btn_activate'], 'btn-CONTROLbActive')
    button_with_up_icon = make_button("ArrowUpColor.svg", tr['btn_up'], 'btn-CONTROLbDisplayUp')
    button_with_down_icon = make_button("ArrowDownColor.svg", tr['btn_down'], 'btn-CONTROLbDisplayDown')

    return button_with_process_icon, button_with_up_icon, button_with_down_icon