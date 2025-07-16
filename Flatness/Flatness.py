import pandas as pd
import numpy as np

from matplotlib.widgets import Button
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from mpl_toolkits.mplot3d import Axes3D  # konieczne do dodania osi 3D


path = r"E:\PP\22_0014_0000 - ADAPTSYS Walcarka\Pomiary\Nowe pomiary demonstratorów na walcarce z wykorzystaniem portalu, obrotnicy i kamery. Dane wpisywane przez operatora\Pomiar blachy 9"
name = r"28BL2406x1206_S4-43_ID186_POM1_2024_02_01_08_32_28.txt"
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
print((df.columns))

# 4. Resetuj indeks jeśli chcesz mieć numery punktów w kolumnie (opcjonalnie)
df = df.reset_index()

# 5. Pobierz kolumny danych
# x= df['Punkty pomiarowe'].values
# y = df['X'].values
# z = df['Y'].values
#z = df['Wartosc Raw'].values

x= df['X'].values
y = df['Y'].values
z = df['Wartosc Raw'].values

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

#fig = plt.figure(figsize=(18,6))
# Tworzymy figurę i definujemy układ gridspec
fig = plt.figure(figsize=(18, 8))
fig.suptitle("28BL2406x1206_S4-43_ID186_POM1_2024_02_01_08_32_28", fontsize=20)
fig.text(0.45, 0.94, f'Płaskość: {flatness:.4f}', ha='left', va='top', fontsize=16)
gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])  # 2 wiersze, 2 kolumny; górny wiersz dwukrotnie wyższy
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()  # przełącza na pełny ekran

# Widok z góry (pl. XY)
ax1 = fig.add_subplot(gs[0, 1], projection='3d')
scat1 = ax1.scatter(x, y, z, c=deviation, cmap='bwr', s=30, vmin=-1, vmax=1)
ax1.plot_surface(X_grid, Y_grid, Z_grid, color='red', alpha=0.4)
ax1.view_init(elev=90, azim=-90)
ax1.set_title('Widok z góry (XY)')
ax1.set_xlim(xlim)
ax1.set_ylim(ylim)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_box_aspect((1,2,0.5))
ax1.set_zlim(z_min_limit, z_max_limit)

# Widok z boku (pl. XZ)
ax2 = fig.add_subplot(gs[1, 1], projection='3d')
scat2 = ax2.scatter(x, y, z, c=deviation, cmap='bwr', s=30, vmin=-1, vmax=1)
ax2.plot_surface(X_grid, Y_grid, Z_grid, color='red', alpha=0.4)
ax2.view_init(elev=0, azim=-90)
ax2.set_title('Widok z boku (XZ)')
ax2.set_xlim(xlim)
ax2.set_ylim(ylim)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_box_aspect((1,2,0.5))
ax2.set_zlim(z_min_limit, z_max_limit)

# Widok pośredni (ukośny) - np. elewacja 45°, azymut -90°
ax3 = fig.add_subplot(gs[:, 0], projection='3d')
scat3 = ax3.scatter(x, y, z, c=deviation, cmap='bwr', s=30, vmin=-1, vmax=1)
ax3.plot_surface(X_grid, Y_grid, Z_grid, color='red', alpha=0.4)
ax3.view_init(elev=45, azim=-45)
ax3.set_title('Widok pośredni (45° ukośny)')
ax3.set_xlim(xlim)
ax3.set_ylim(ylim)
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.set_box_aspect((1,2,0.5))
ax3.set_zlim(z_min_limit, z_max_limit)


# Jeden wspólny pasek kolorów dla wszystkich trzech wykresów
cbar = plt.colorbar(scat1, ax=[ax1, ax2, ax3], shrink=0.6, pad=0.05)
cbar.set_label('Odchylenie od płaszczyzny')

# miejsce pod wykresami
ax_button = plt.axes([0.45, 0.01, 0.1, 0.05])  # [left, bottom, width, height]
button = Button(ax_button, 'Reset View')

# Funkcja resetująca widok obu wykresów do wartości domyślnych
def reset(event):
    ax1.view_init(elev=90, azim=-90)
    ax2.view_init(elev=0, azim=-90)
    ax3.view_init(elev=45, azim=-45)
    fig.canvas.draw_idle()

def update(frame):
    azim = -90 + 180 * (frame / 50)  # zmienia azymut od -90 do 90 stopni
    ax3.view_init(azim=azim)
    return []

button.on_clicked(reset)

#plt.tight_layout() # Dopasowanie układu subplots
anim = FuncAnimation(fig, update, frames=50, interval=5)
plt.show()