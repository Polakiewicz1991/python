import numpy as np
import pandas as pd

def calculate_flatness(df):
    """
    Oblicza płaskość powierzchni na podstawie punktów 3D.

    Parametry:
      df (pandas.DataFrame): zawiera kolumny 'x', 'y', 'z'

    Zwraca:
      flatness (float): różnica max i min odchylenia od dopasowanej płaszczyzny
      coeffs (np.array): współczynniki (a, b, c) równania płaszczyzny z = a*x + b*y + c
    """
    x = df['x'].to_numpy() # 1. Pobranie kolumny 'x' z DataFrame i konwersja do jednowymiarowej tablicy numpy
    y = df['y'].to_numpy() # 2. Pobranie kolumny 'y' z DataFrame i konwersja do jednowymiarowej tablicy numpy
    z = df['z'].to_numpy() # 3. Pobranie kolumny 'z' z DataFrame i konwersja do jednowymiarowej tablicy numpy

    # 4. Konstrukcja macierzy współczynników A, gdzie:
    #    - np.c_ łączy kolumnowo wektory: x, y oraz wektor jedynek (współczynnik przy wyrazie wolnym c)
    #    - Macierz A ma kształt (n_punktów, 3) i reprezentuje układ równań liniowych do dopasowania płaszczyzny
    A = np.c_[x, y, np.ones_like(x)]

    # 5. Dopasowanie płaszczyzny z = a*x + b*y + c metodą najmniejszych kwadratów:
    #    - szukamy wektora [a,b,c], który minimalizuje ||A @ [a,b,c] - z||^2
    #    - funkcja zwraca współczynniki (coeffs) oraz kilka dodatkowych informacji (residuals, rank macierzy A itp.)

    coeffs, residuals, rank, s = np.linalg.lstsq(A, z, rcond=None)

    # 6. Rozpakowanie współczynników równania płaszczyzny
    a, b, c = coeffs

    # 7. Obliczenie przewidywanych wartości z na płaszczyźnie dopasowanej
    #    dla każdego punktu (x,y)
    z_fit = a * x + b * y + c

    # 8. Wyliczenie odchylenia każdego punktu od tej idealnej płaszczyzny (różnica zmierzonego z i przewidywanego)
    deviations = z - z_fit

    # 9. Płaskość zdefiniowana jako zakres (różnica max i min) tych odchyleń
    #    Taki wskaźnik informuje o rozrzucie punktów względem dopasowanej płaszczyzny,
    #    czyli jak „gruba” lub nierówna jest powierzchnia.
    flatness = deviations.max() - deviations.min()

    # 10. Zwrócenie wartości płaskości oraz współczynników płaszczyzny dla dalszej analizy lub wizualizacji
    return flatness, coeffs, deviations