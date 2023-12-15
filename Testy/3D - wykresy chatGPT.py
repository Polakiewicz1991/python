import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.animation import FuncAnimation

# Funkcja do generowania przypadkowych danych wektorów
def generate_random_vectors():
    positions = np.random.rand(6, 3)
    directions = np.random.rand(6, 3)
    directions /= np.linalg.norm(directions, axis=1, keepdims=True)  # Normalizacja wektorów kierunkowych
    return positions, directions

# Inicjalizacja danych
positions, directions = generate_random_vectors()

# Inicjalizacja wykresu 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Inicjalizacja wektorów jako pustych obiektów
quivers = [ax.quiver(0, 0, 0, 0, 0, 0) for _ in range(6)]

# Ustawienia osi
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Funkcja aktualizacji animacji
def update(frame):
    # Aktualizacja danych wektorów
    positions, directions = generate_random_vectors()

    # Aktualizacja wektorów na wykresie
    for quiver, pos, dir in zip(quivers, positions, directions):
        quiver = ax.quiver(pos[0], pos[1], pos[2], dir[0], dir[1], dir[2], color='b')

# Utworzenie animacji
ani = FuncAnimation(fig, update, frames=range(100), interval=100, repeat=False)

# Wyświetlenie animacji
plt.show()