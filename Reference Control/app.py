from dash import Dash
from layout import create_layout
from callbacks import register_callbacks
from data_utils import read_all_csv_in_folder

FOLDER_PATH = "./Reference edited"  # folder z plikami .csv

all_data = read_all_csv_in_folder(FOLDER_PATH)

app = Dash(__name__)
app.title = "CSV Viewer"

app.layout = create_layout(list(all_data.keys()))

register_callbacks(app, all_data)

if __name__ == "__main__":
    app.run(debug=True)
