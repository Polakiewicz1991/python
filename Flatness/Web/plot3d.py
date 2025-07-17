import plotly.graph_objs as go
import numpy as np

def create_3d_scatter(df,coeffs,deviations):

    a, b, c = coeffs

    # Tworzymy unikalne, uporządkowane wartości X i Y (zakładamy, że są numeryczne)
    x_unique = np.sort(df['x'].unique())
    y_unique = np.sort(df['y'].unique())

    # Tworzymy siatkę współrzędnych X, Y
    X, Y = np.meshgrid(x_unique, y_unique)

    # Tworzymy macierz Z dopasowując wartości do siatki
    # Metoda pivot_table wygeneruje tablicę z wartościami z kolumny 'z' zorganizowaną wg x i y
    Z_df = df.pivot_table(index='y', columns='x', values='z')
    Z = Z_df.values - c

    # 1. Tworzymy trace typu Scatter3d - pojedynczy zbiór punktów 3D na wykresie
    scatter = go.Surface(
        x=X, # 2. Współrzędne X punktów - pobierane jako tablica numpy
        y=Y, # 3. Współrzędne y punktów - pobierane jako tablica numpy
        z=Z, # 4. Współrzędne z punktów - pobierane jako tablica numpy
        #mode='markers',   # 5. Tryb wyświetlania punktów – same znaczniki (markery), bez linii
        # marker=dict(        # 6. Parametry znaczników (markerów)
        #     size=5,         # 7. Rozmiar każdego punktu na wykresie
        #     color=deviations,      # 8. Kolor punktów określany przez wartości deviations
        #     colorscale=[
        #         [0, 'blue'],  # kolor dla minimalnej wartości (0)
        #         [0.5, 'white'],  # kolor dla minimalnej wartości (0)
        #         [1, 'red']  # kolor dla maksymalnej wartości (1)
        #     ],
        colorscale=[
            [0, 'blue'],  # kolor dla minimalnej wartości (0)
            [0.5, 'white'],  # kolor dla minimalnej wartości (0)
            [1, 'red']
        ],  # kolor dla maksymalnej wartości (1)
        opacity=0.8, # 10. Przezroczystość markerów (80%)
        colorbar=dict(title='Z value')  # 11. Pasek kolorów pokazujący skalę wartości Z
        )

    # IDEALNA PŁASZCZYZNA


    # Punkt 1: siatka x, y do narysowania powierzchni płaszczyzny
    x_range = np.linspace(df['x'].min(), df['x'].max(), 30)
    y_range = np.linspace(df['y'].min(), df['y'].max(), 30)
    X_grid, Y_grid = np.meshgrid(x_range, y_range)

    # Punkt 2: obliczenie Z płaszczyzny na siatce
    Z_grid = a * X_grid + b * Y_grid #+ c

    # Punkt 4: trace powierzchni płaszczyzny
    plane = go.Surface(
        x=X_grid,
        y=Y_grid,
        z=Z_grid,
        colorscale=[
            [0,'gray'],
            [1,'gray']
        ],
        opacity=0.5,
        showscale=False  # wyłącz pasek skali kolorów dla płaszczyzny jeśli nie potrzeba
    )

    # 12. Tworzymy figurę Plotly i dodajemy do niej listę trace (tu tylko jeden trace - scatter)
    fig = go.Figure(data=[scatter,plane])

    # 13. Modyfikujemy layout wykresu - czyli jego ogólny wygląd i parametry osi
    fig.update_layout(
        margin=dict(l=0, r=0, b=0, t=40),       # 14. Marginesy wykresu: left, right, bottom zero, top 40 px dla tytułu
        scene=dict(                             # 15. Konfiguracja "scene" - układu osi 3D
            xaxis_title='X',                    # 16. Etykieta osi X
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode = 'manual',
            aspectratio = dict(x=1, y=2, z=1)
        ),
        title='Interaktywny wykres 3D'          # 19. Tytuł całego wykresu
    )

    # 20. Zwracamy gotową figurę Plotly, którą można wyświetlić w przeglądarce/komponentach Dash
    return fig