from dash import Dash
from layout import get_layout
import callbacks

app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Wykres 3D - CSV & Płaskość"

app.layout = get_layout()  # teraz to layout z zakładkami

callbacks.register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)