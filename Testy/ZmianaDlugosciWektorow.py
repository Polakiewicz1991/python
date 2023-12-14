import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np

# Dane początkowe
x = [0, 1]
y = [0, 1]
z = [0, 0]
dx = [1, 0]
dy = [0, 1]
dz = [0, 0]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
quiver = ax.quiver(x, y, z, dx, dy, dz, color=['r', 'b'])

def update(frame):
    # Symulacja zmiany długości i pozycji wektorów
    scale_factor = 1 + np.sin(frame * 0.1)  # Symulacja zmiany długości
    x[1] = scale_factor  # Zmiana pozycji drugiego wektora

    # Aktualizacja wektorów
    quiver.remove()  # Usunięcie poprzednich wektorów
    quiver = ax.quiver(x, y, z, dx, dy, dz, color=['r', 'b'])

ani = FuncAnimation(fig, update, frames=np.arange(0, 2 * np.pi, 0.1), interval=50)
plt.show()