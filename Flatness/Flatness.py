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

# Dopasowanie płaszczyzny metodą najmniejszych kwadratów
# Funkcja celu: z = a*x + b*y + c
A = np.c_[x, y, np.ones(x.shape)]
coeffs, residuals, rank, s = np.linalg.lstsq(A, z, rcond=None)
a, b, c = coeffs

print(f'Dopasowana płaszczyzna: z = {a:.5f}*x + {b:.5f}*y + {c:.5f}')

# Oblicz wartości płaszczyzny dla punktów pomiarowych
z_fit = a * x + b * y + c

# Oblicz płaskość jako różnicę max-min odchyleń od płaszczyzny
flatness = np.max(z - z_fit) - np.min(z - z_fit)
print(f'Płaskość (odchylenie od dopasowanej płaszczyzny): {flatness:.4f}')

# Rysowanie wykresu 3D z punktami
fig = plt.figure(figsize=(14, 7))

# Wykres punktów powierzchni rzeczywistej
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')
ax1.set_title('Wizualizacja rzeczywistej powierzchni')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Wartosc Raw')

# Wykres dopasowanej płaszczyzny (pierwszy subplot)
ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(x, y, z - z_fit, c='r', label='Odchylenia od płaszczyzny', s=10)
# Można też narysować samą płaszczyznę jako siatkę:
# Utwórz siatkę do rysowania płaszczyzny
x_lin = np.linspace(np.min(x), np.max(x), 50)
y_lin = np.linspace(np.min(y), np.max(y), 50)
X_grid, Y_grid = np.meshgrid(x_lin, y_lin)
Z_grid = a * X_grid + b * Y_grid + c
ax2.plot_surface(X_grid, Y_grid, Z_grid, alpha=0.5, color='cyan')
ax2.set_title('Dopasowana płaszczyzna odniesienia + odchylenia')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Odchylenie')

plt.tight_layout()
plt.show()