from dash import Dash
from Flatness.Web.layouts.main_layout import get_layout
from Flatness.Web.callbacks.callback_tabs import register_callbacks as register_callbacks_tabs
from Flatness.Web.callbacks.callbacks_plots import register_callbacks as register_callbacks_plots
from Flatness.Web.callbacks.callbacks_plc import register_callbacks as register_callbacks_plc

app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Wykres 3D - CSV & Płaskość"

app.layout = get_layout()  # teraz to layout z zakładkami

register_callbacks_tabs(app)
register_callbacks_plots(app)
register_callbacks_plc(app)

if __name__ == "__main__":
    app.run(debug=True)