import math

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.animation import FuncAnimation

from ForwardKinematicsPuma import x, y, z, colors, Fi

# Rysowanie wektorów 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

a = []
dx = []
dy = []
dz = []

for i in range(len(x) - 1):
    dx.append(x[i + 1] - x[i])
    dy.append(y[i + 1] - y[i])
    dz.append(z[i + 1] - z[i])
    a.append(math.sqrt(((x[i + 1] - x[i])**2) + ((y[i + 1] - y[i])**2) + ((z[i + 1] - z[i])**2)))

    ax.quiver(x[i], y[i], z[i], dx[i], dy[i], dz[i], length=a[i], normalize=True, color=colors[i])

# Dodawanie etykiet z współrzędnymi na końcu każdego wektora
for i in range(len(x)):
    if i < len(x) - 1:
        ax.text(round((x[i]), 3), round((y[i]), 3), round((z[i]), 3), f'({float(round((x[i]),2)):2.2f},'
                                                                      f' {float(round((y[i]),2)):2.2f},'
                                                                      f' {float(round((z[i]),2)):2.2f},'
                                                                      f' {math.degrees(Fi[i])}[°])')
    else:
        ax.text(round((x[i]), 3), round((y[i]), 3), round((z[i]), 3), f'({float(round((x[i]), 2)):2.2f},'
                                                                      f' {float(round((y[i]), 2)):2.2f},'
                                                                      f' {float(round((z[i]), 2)):2.2f})')


# Ustawienia osi
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-20, 20])

# Wyświetlenie wykresu
plt.title('Rysowanie Wektorów 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()