from dash import Dash, html, Input, Output
from layout import serve_layout
from callbacks import register_callbacks
from data_utils import read_all_csv_in_folder
import dash

FOLDER_PATH = "./csv_data"
all_data = read_all_csv_in_folder(FOLDER_PATH)

app = Dash(__name__)
app.title = "CSV Compare Tool"
app.layout = serve_layout(all_data)

register_callbacks(app, all_data)

# --- Run server ---
if __name__ == "__main__":
    app.run(debug=True)
