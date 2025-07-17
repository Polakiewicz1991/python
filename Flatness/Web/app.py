from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go

from data_handler import parse_csv
from flatness_calculator import calculate_flatness
from plot3d import create_3d_scatter

# Inicjalizacja aplikacji Dash
app = Dash(__name__)
app.title = "Wykres 3D - CSV & Płaskość"

# Layout aplikacji
app.layout = html.Div([
    html.H2("Wczytaj plik CSV z danymi 3D (x;y;z)"),
    dcc.Upload(
        id='upload-data',
        children=html.Button('Przeglądaj i załaduj CSV'),
        multiple=False,
        accept='.csv'
    ),
    html.Div(id='flatness-output', style={'marginTop': '20px', 'fontWeight': 'bold'}),
    dcc.Graph(id='3d-plot', style={'height': '600px', 'marginTop': '20px'})
])

# Callback obsługujący wczytanie pliku, obliczenia i rysowanie wykresu
@app.callback(
    Output('3d-plot', 'figure'),
    Output('flatness-output', 'children'),
    Input('upload-data', 'contents')
)
def update_output(contents):
    if contents is None:
        # Wykres pusty i brak wyniku przed załadowaniem pliku
        empty_fig = go.Figure()
        empty_fig.update_layout(title='Wczytaj plik CSV, aby wyświetlić wykres')
        return empty_fig, ""

    try:
        df = parse_csv(contents)
    except Exception as e:
        # Obsługa błędów parsowania lub walidacji
        empty_fig = go.Figure()
        empty_fig.update_layout(title=f"Błąd wczytywania pliku: {str(e)}")
        return empty_fig, ""

    flatness_value, coeffs, deviations = calculate_flatness(df)
    print("coffes:\n", coeffs,'\n')
    fig = create_3d_scatter(df,coeffs,deviations)
    flatness_text = f"Płaskość powierzchni (metodą najmniejszych kwadratów: {flatness_value:.4f}"

    return fig, flatness_text

# Uruchomienie aplikacji
if __name__ == '__main__':
    app.run(debug=True)