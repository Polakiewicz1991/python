import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
from mpl_toolkits.mplot3d import Axes3D  # konieczne do dodania osi 3D


path = r"E:\PP\22_0014_0000 - ADAPTSYS Walcarka\Pomiary\Nowe pomiary demonstratorów na walcarce z wykorzystaniem portalu, obrotnicy i kamery. Dane wpisywane przez operatora\Pomiar blachy 31"
name = r"28X2400X1200_ID10_POM1_2023_07_14_09_18_16.txt"
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

# Ustawienie stałego zakresu dla osi Z, jeśli jest potrzebne (z Twojego przykładu)
z_min_limit = 15
z_max_limit = 18

fig = plt.figure(figsize=(14, 6)) # Większy rozmiar figury

# --- Pierwszy wykres: Rzut z góry (widok na płaszczyznę XY) ---
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
scat1 = ax1.scatter(x, y, z, c=deviation, cmap='bwr', s=30, vmin=-1, vmax=1, depthshade=False)
ax1.plot_surface(X_grid, Y_grid, Z_grid, color='red', alpha=0.4)

ax1.view_init(elev=90, azim=-90) # elewacja = 90° (patrzymy z góry), azymut = -90° (oś Y "do góry")
ax1.set_title('Widok z góry (płaszczyzna XY)')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Wartość Z') # Zamiast 'Wartość Raw' dla ogólności

ax1.set_xlim(xlim) # Utrzymaj te same limity dla porównania
ax1.set_ylim(ylim)
ax1.set_zlim(z_min_limit, z_max_limit) # Ustaw stały zakres Z

# --- Drugi wykres: Rzut z boku (widok na płaszczyznę XZ) ---
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
scat2 = ax2.scatter(x, y, z, c=deviation, cmap='bwr', s=30, vmin=-1, vmax=1, depthshade=False)
ax2.plot_surface(X_grid, Y_grid, Z_grid, color='red', alpha=0.4)

ax2.view_init(elev=0, azim=-90) # elewacja = 0° (patrzymy na poziomie), azymut = -90° (patrzymy na płaszczyznę XZ)
ax2.set_title('Widok z boku (płaszczyzna XZ)')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Wartość Z')

ax2.set_xlim(xlim) # Utrzymaj te same limity dla porównania
ax2.set_ylim(ylim)
ax2.set_zlim(z_min_limit, z_max_limit) # Ustaw stały zakres Z

# Wspólny pasek kolorów dla obu wykresów
cbar = plt.colorbar(scat1, ax=[ax1, ax2], shrink=0.6, pad=0.05) # Pad dostosowany do 2 subplotów
cbar.set_label('Odchylenie od płaszczyzny (dodatnie - czerwone, ujemne - niebieskie)')

# miejsce pod wykresami
ax_button = plt.axes([0.45, 0.01, 0.1, 0.05])  # [left, bottom, width, height]
button = Button(ax_button, 'Reset View')

# Funkcja resetująca widok obu wykresów do wartości domyślnych
def reset(event):
    ax1.view_init(elev=90, azim=-90)
    ax2.view_init(elev=0, azim=-90)
    fig.canvas.draw_idle()

button.on_clicked(reset)

#plt.tight_layout() # Dopasowanie układu subplots
plt.show()