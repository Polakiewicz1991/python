import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # konieczne do dodania osi 3D

filename = r"E:\PP\22_0014_0000 - ADAPTSYS Walcarka\Pomiary\Nowe pomiary demonstratorów na walcarce z wykorzystaniem portalu, obrotnicy i kamery. Dane wpisywane przez operatora\Pomiar blachy 40\28X2400X1200_ID21_POM2_2023_07_17_11_40_40.txt"

# 1. Znajdź linię nagłówka rozpoczynającą się od "Punkty pomiarowe:"
header_line = None
with open(filename, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if line.strip().startswith('Punkty pomiarowe:'):
            header_line = i
            break
if header_line is None:
    raise ValueError("Nie znaleziono nagłówka danych")

# 2. Wczytaj dane
# Jeśli separator tabulator nie działa (np. plik ma spacje), spróbuj sep=r'\s+' z engine='python'
df = pd.read_csv(
    filename,
    sep='\t',
    skiprows=header_line,
    header=0,
    index_col=0,
    encoding='utf-8'
)

# 3. Usuń dwukropki i spacje z nazw kolumn
df.columns = [col.strip().replace(':', '') for col in df.columns]

# 4. Resetuj indeks jeśli chcesz mieć numery punktów w kolumnie (opcjonalnie)
df = df.reset_index()

# 5. Pobierz kolumny danych
x= df['Punkty pomiarowe'].values
y = df['X'].values
z = df['Y'].values
#z = df['Wartosc Raw'].values

flatness = z.max() - z.min()
print(f'Płaskość: {flatness:.4f}')

# 3. Dopasowanie płaszczyzny metodą najmniejszych kwadratów: z = a*x + b*y + c
A = np.c_[x, y, np.ones_like(x)]
coeffs, _, _, _ = np.linalg.lstsq(A, z, rcond=None)
a, b, c = coeffs
print(f'Dopasowana płaszczyzna: z = {a:.5f}*x + {b:.5f}*y + {c:.5f}')

# 4. Oblicz wartości płaszczyzny odniesienia w punktach (x,y)
z_plane = a*x + b*y + c

# 5. Rysowanie obydwu powierzchni na jednej osi 3D
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

# Powierzchnia rzeczywista z pomiarów
surf_data = ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none', alpha=0.8)

# Idealna płaszczyzna odniesienia - narysowana jako przezroczysta powierzchnia
surf_plane = ax.plot_trisurf(x, y, z_plane, color='red', alpha=0.4, edgecolor='none')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Wartosc Raw i płaszczyzna odniesienia')
plt.title('Płaskość blachy z dopasowaną płaszczyzną odniesienia')
plt.show()