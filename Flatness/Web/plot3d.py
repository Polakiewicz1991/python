import plotly.graph_objs as go
import numpy as np

from Flatness.Web.layouts.translations import translations

def create_3d_scatter(df,coeffs,deviations, lang='pl', view='main'):
    # wybór tytułu zależnie od widoku
    tr = translations.get(lang, translations['pl'])
    title = tr.get(f'chart_{view}', tr['chart_main'])

    a, b, c = coeffs

    # Tworzymy unikalne, uporządkowane wartości X i Y (zakładamy, że są numeryczne)
    x_unique = np.sort(df['x'].unique())
    y_unique = np.sort(df['y'].unique())

    # Tworzymy siatkę współrzędnych X, Y
    X, Y = np.meshgrid(x_unique, y_unique)

    # Tworzymy macierz Z dopasowując wartości do siatki
    # Metoda pivot_table wygeneruje tablicę z wartościami z kolumny 'z' zorganizowaną wg x i y
    #Z_df = df.pivot_table(index='y', columns='x', values='z')
    #Z = Z_df.values - c
    # Dopasowanie odchyleń do siatki
    dev_df = df.copy()
    dev_df['deviation'] = deviations
    Z_df = dev_df.pivot_table(index='y', columns='x', values='deviation')
    Z = Z_df.values  # teraz mamy odchylenia, a nie z

    # 1. Tworzymy trace typu Scatter3d - pojedynczy zbiór punktów 3D na wykresie
    scatter = go.Surface(
        x=X, # 2. Współrzędne X punktów - pobierane jako tablica numpy
        y=Y, # 3. Współrzędne y punktów - pobierane jako tablica numpy
        z=Z, # 4. Współrzędne z punktów - pobierane jako tablica numpy
        colorscale=[
            [0, 'blue'],  # kolor dla minimalnej wartości (0)
            [0.5, 'white'],  # kolor dla minimalnej wartości (0)
            [1, 'red']
        ],  # kolor dla maksymalnej wartości (1)
        opacity=0.8, # 10. Przezroczystość markerów (80%)
        colorbar=dict(title='Z value')  # 11. Pasek kolorów pokazujący skalę wartości Z
        )
    # 🔹 Ustal zakres kolorów symetrycznie względem 0
    max_dev = max(abs(Z.min()), abs(Z.max()))

    # 🔹 Zaktualizuj tylko parametry koloru (bez zmiany geometrii!)
    scatter.update(
        cmin=-max_dev,
        cmax=max_dev,
        colorscale=[
            [0, 'blue'],
            [0.5, 'white'],
            [1, 'red']
        ],
        colorbar=dict(title='Odchylenie [mm]')
    )
    # IDEALNA PŁASZCZYZNA

    # Punkt 1: siatka x, y do narysowania powierzchni płaszczyzny
    x_range = np.linspace(df['x'].min(), df['x'].max(), 30)
    y_range = np.linspace(df['y'].min(), df['y'].max(), 30)
    X_grid, Y_grid = np.meshgrid(x_range, y_range)

    # Punkt 2: obliczenie Z płaszczyzny na siatce
    #Z_grid = a * X_grid + b * Y_grid #+ c
    Z_grid = np.zeros_like(X_grid)

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
            xaxis_title='Y',                    # 16. Etykieta osi X
            yaxis_title='X',
            zaxis_title='Z',
            aspectmode = 'manual',
            aspectratio = dict(x=1, y=2, z=1)
        ),
        title=title          # 19. Tytuł całego wykresu
    )

    # 20. Zwracamy gotową figurę Plotly, którą można wyświetlić w przeglądarce/komponentach Dash
    return fig

def create_3d_scatter_no_bar(df,coeffs,deviations, lang='pl', view='main'):
    # wybór tytułu zależnie od widoku
    tr = translations.get(lang, translations['pl'])
    title = tr.get(f'chart_{view}', tr['chart_main'])

    a, b, c = coeffs

    # Tworzymy unikalne, uporządkowane wartości X i Y (zakładamy, że są numeryczne)
    x_unique = np.sort(df['x'].unique())
    y_unique = np.sort(df['y'].unique())

    # Tworzymy siatkę współrzędnych X, Y
    X, Y = np.meshgrid(x_unique, y_unique)

    # Tworzymy macierz Z dopasowując wartości do siatki
    # Metoda pivot_table wygeneruje tablicę z wartościami z kolumny 'z' zorganizowaną wg x i y
    #Z_df = df.pivot_table(index='y', columns='x', values='z')
    #Z = Z_df.values - c
    # Dopasowanie odchyleń do siatki
    dev_df = df.copy()
    dev_df['deviation'] = deviations
    Z_df = dev_df.pivot_table(index='y', columns='x', values='deviation')
    Z = Z_df.values  # teraz mamy odchylenia, a nie z

    # 1. Tworzymy trace typu Scatter3d - pojedynczy zbiór punktów 3D na wykresie
    scatter = go.Surface(
        x=X, # 2. Współrzędne X punktów - pobierane jako tablica numpy
        y=Y, # 3. Współrzędne y punktów - pobierane jako tablica numpy
        z=Z, # 4. Współrzędne z punktów - pobierane jako tablica numpy
        colorscale=[
            [0, 'blue'],  # kolor dla minimalnej wartości (0)
            [0.5, 'white'],  # kolor dla minimalnej wartości (0)
            [1, 'red']
        ],  # kolor dla maksymalnej wartości (1)
        opacity=0.8, # 10. Przezroczystość markerów (80%)
        colorbar=dict(title='Z value')  # 11. Pasek kolorów pokazujący skalę wartości Z
        )
    # 🔹 Ustal zakres kolorów symetrycznie względem 0
    max_dev = max(abs(Z.min()), abs(Z.max()))

    # 🔹 Zaktualizuj tylko parametry koloru (bez zmiany geometrii!)
    scatter.update(
        cmin=-max_dev,
        cmax=max_dev,
        colorscale=[
            [0, 'blue'],
            [0.5, 'white'],
            [1, 'red']
        ],
        colorbar=dict(title='Odchylenie [mm]')     ,
        showscale=False  # wyłącz pasek skali kolorów dla płaszczyzny jeśli nie potrzeba
    )
    # IDEALNA PŁASZCZYZNA

    # Punkt 1: siatka x, y do narysowania powierzchni płaszczyzny
    x_range = np.linspace(df['x'].min(), df['x'].max(), 30)
    y_range = np.linspace(df['y'].min(), df['y'].max(), 30)
    X_grid, Y_grid = np.meshgrid(x_range, y_range)

    # Punkt 2: obliczenie Z płaszczyzny na siatce
    #Z_grid = a * X_grid + b * Y_grid #+ c
    Z_grid = np.zeros_like(X_grid)

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
            xaxis_title='Y',                    # 16. Etykieta osi X
            yaxis_title='X',
            zaxis_title='Z',
            aspectmode = 'manual',
            aspectratio = dict(x=1, y=2, z=1)
        ),
        title=title          # 19. Tytuł całego wykresu
    )

    # 20. Zwracamy gotową figurę Plotly, którą można wyświetlić w przeglądarce/komponentach Dash
    return fig