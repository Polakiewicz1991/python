import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

from ForwardKinematicsPuma import x0, x1, x2, x3, x4, x5, x6, x7, x8
from ForwardKinematicsPuma import y0, y1, y2, y3, y4, y5, y6, y7, y8
from ForwardKinematicsPuma import z0, z1, z2, z3, z4, z5, z6, z7, z8
from ForwardKinematicsPuma import a1, a3, a4

# Przykładowe dane - wektory jako punkty początkowe (x, y, z) i składowe wektorów (dx, dy, dz)
x = [x0, x1, x2, x3, x4, x5, x6, x7, x8]
y = [y0, y1, y2, y3, y4, y5, y6, y7, y8]
z = [z0, z1, z2, z3, z4, z5, z6, z7, z8]

dx = [x1, x2, x3, x4, x5, x6, x7, x8, 0]
dy = [x1, x2, x3, x4, x5, x6, x7, x8, 0]
dz = [x1, x2, x3, x4, x5, x6, x7, x8, 0]

# Rysowanie wektorów 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(x0, y0, z0, x1, y1, z1, length=a1, normalize=True, color=['r', 'g', 'b'])
ax.quiver(x1, y1, z1, x2, y2, z2, length=0, normalize=True, color=['r', 'g', 'b'])
ax.quiver(x2, y2, z2, x3, y3, z3, length=0, normalize=True, color=['r', 'g', 'b'])
ax.quiver(x3, y3, z3, x4, y4, z4, length=a3, normalize=True, color=['r', 'g', 'b'])
ax.quiver(x4, y4, z4, x5, y5, z5, length=a4, normalize=True, color=['r', 'g', 'b'])
ax.quiver(x5, y5, z5, x6, y6, z6, length=0, normalize=True, color=['r', 'g', 'b'])
ax.quiver(x6, y6, z5, x7, y7, z7, length=0, normalize=True, color=['r', 'g', 'b'])
ax.quiver(x7, y7, z6, x8, y8, z8, length=0, normalize=True, color=['r', 'g', 'b'])
ax.quiver(x8, y8, z8, 0, 0, 0, length=0, normalize=True, color=['r', 'g', 'b'])

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