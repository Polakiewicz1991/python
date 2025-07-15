import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # konieczne do dodania osi 3D


path = r"E:\PP\22_0014_0000 - ADAPTSYS Walcarka\Pomiary\Nowe pomiary demonstratorów na walcarce z wykorzystaniem portalu, obrotnicy i kamery. Dane wpisywane przez operatora\Pomiar blachy 37"
name = r"28X2400X1200_ID29_POM1_2023_07_19_10_32_47.txt"
filename = path + '\\' + name

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

# Dopasowanie płaszczyzny
A = np.c_[x, y, np.ones_like(x)]
coeffs, _, _, _ = np.linalg.lstsq(A, z, rcond=None)
a, b, c = coeffs
z_plane = a*x + b*y + c

# Obliczanie odchylenia od płaszczyzny
deviation = z - z_plane  # wartości dodatnie i ujemne

xlim = [x.min(), x.max()]
ylim = [y.min(), y.max()]
X_grid, Y_grid = np.meshgrid(np.linspace(*xlim, 10), np.linspace(*ylim, 10))

# Obliczamy Z na podstawie równania płaszczyzny
Z_grid = a * X_grid + b * Y_grid + c

# Rysowanie punktów z kolorowaniem heatmapą divergencką (czerwononiebieską)
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

scat = ax.scatter(x, y, z, c=deviation, cmap='bwr', s=30)
# Idealna płaszczyzna odniesienia (przezroczysta)
ax.plot_surface(X_grid, Y_grid, Z_grid, color='red', alpha=0.4)
# Dodaj pasek kolorów z etykietami
cbar = plt.colorbar(scat, ax=ax, shrink=0.6, pad=0.1)
cbar.set_label('Odchylenie od płaszczyzny (dodatnie-czerwone, ujemne-niebieskie)')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Wartosc Raw')
plt.title('Heatmapa odchyleń od płaszczyzny idealnej')

plt.show()