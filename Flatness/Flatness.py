import pandas as pd
import matplotlib.pyplot as plt
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

# 6. Upewnij się, że dane są numeryczne (łatwe do poprawienia, jeśli nie)
for col in ['Punkty pomiarowe', 'X', 'Y', 'Wartosc Raw']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 7. Wykres 3D z triangulacją
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

# plot_trisurf wymaga 1D tablic x,y,z punktów, tworzy siatkę trójkątną
ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Wartosc Raw')
plt.title('Wizualizacja płaskości blachy')
plt.show()