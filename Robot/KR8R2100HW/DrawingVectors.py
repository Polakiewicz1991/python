import math
from random import randrange
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.animation import FuncAnimation

from RobotDefinition import robotKR8R2100HW as robot

# Rysowanie wektorów 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(robot)):

    r, g, b = randrange(0,100) / 100, randrange(0,100) / 100, randrange(0,100) / 100,

    ax.quiver(robot[i].pos["x"], robot[i].pos["y"], robot[i].pos["z"],
              robot[i].dir["x"], robot[i].dir["y"], robot[i].dir["z"],
              length=robot[i].lenght, normalize=True, color=(r,g,b,1))
    ax.text(robot[i].pos["x"], robot[i].pos["y"], robot[i].pos["z"],    f'({(robot[i].pos["x"]):2.2f},'
                                                                        f' {(robot[i].pos["y"]):2.2f},'
                                                                        f' {(robot[i].pos["z"]):2.2f},'
                                                                        f' {(robot[i].theta):2.2f}[°])')

# Ustawienia osi
ax.set_xlim([-2200, 2200])
ax.set_ylim([-2200, 2200])
ax.set_zlim([-1000, 2200])

# Wyświetlenie wykresu
plt.title('Rysowanie Wektorów 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()