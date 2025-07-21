from dash import Dash, dcc, html, Input, Output, State, ctx, no_update
import plotly.graph_objs as go

from data_handler import parse_csv
from flatness_calculator import calculate_flatness
from plot3d import create_3d_scatter

# Inicjalizacja aplikacji Dash
app = Dash(__name__)
app.title = "Wykres 3D - CSV & Płaskość"

# Wartości domyślne kamery (reset view)
default_camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=1.25, y=2, z=1.25)
)

# Layout aplikacji
app.layout = html.Div([
    html.H2("Wczytaj plik CSV z danymi 3D (x;y;z)"),

    # Kontener flex - przyciski ułożone w linii
    html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Button('Przeglądaj i załaduj CSV')
        ),

        html.Button("Resetuj widok", id='reset-view-btn', n_clicks=0)
    ], style={
        'display': 'flex',       # Flexbox włączony - dzieci obok siebie
        'gap': '10px',           # Odstęp między przyciskami
        'alignItems': 'center'   # Pionowe wyrównanie do środka
    }),

    html.Div(id='flatness-output', style={'marginTop': '20px', 'fontWeight': 'bold'}),
    dcc.Graph(id='3d-plot', style={'height': '600px', 'marginTop': '20px'})
])

# Callback obsługujący upload i reset widoku
@app.callback(
    Output('3d-plot', 'figure'),
    Output('flatness-output', 'children'),
    Input('upload-data', 'contents'),
    Input('reset-view-btn', 'n_clicks'),
    State('3d-plot', 'figure'),
)
def update_or_reset(contents, n_clicks, fig):
    triggered_id = ctx.triggered_id if hasattr(ctx, "triggered_id") else None

    # 1. Jeśli ładowanie pliku
    if triggered_id == 'upload-data':
        if contents is None:
            empty_fig = go.Figure()
            empty_fig.update_layout(title='Wczytaj plik CSV, aby wyświetlić wykres')
            return empty_fig, ""
        try:
            df = parse_csv(contents)
        except Exception as e:
            empty_fig = go.Figure()
            empty_fig.update_layout(title=f"Błąd wczytywania pliku: {str(e)}")
            return empty_fig, ""
        flatness_value, coeffs, deviations = calculate_flatness(df)
        fig_new = create_3d_scatter(df, coeffs, deviations)
        flatness_text = f"Płaskość powierzchni (metodą najmniejszych kwadratów): {flatness_value:.4f}"
        # Ustaw kamerę domyślną przy nowych danych
        fig_new.update_layout(scene_camera=default_camera)
        return fig_new, flatness_text

    # 2. Jeśli reset widoku
    elif triggered_id == 'reset-view-btn' and fig is not None:
        fig['layout']['scene']['camera'] = default_camera
        return fig, no_update

    # 3. Inne przypadki: pusta scena na starcie
    empty_fig = go.Figure()
    empty_fig.update_layout(title='Wczytaj plik CSV, aby wyświetlić wykres')
    return empty_fig, ""

# Uruchomienie aplikacji
if __name__ == '__main__':
    app.run(debug=True)