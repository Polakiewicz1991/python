import math
from random import randrange
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from RobotDefinition import robotKR8R2100HW

# Rysowanie wykresu 3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# Konfiguracja animacji ruchu
# t_stop = 2.5  # how many seconds to simulate
# history_len = 500  # how many trajectory points to display
# dt = 0.01
# t = np.arange(0, t_stop, dt)# create a time array from 0..t_stop sampled at 0.02 second steps

def drawindA3DChart(robot):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Ustawienia osi
    ax.set_xlim([-2200, 2200])
    ax.set_ylim([-2200, 2200])
    ax.set_zlim([-1000, 2200])

    for i in range(len(robot)):
        r, g, b = randrange(0, 100) / 100, randrange(0, 100) / 100, randrange(0, 100) / 100,

        ax.quiver(robot[i].pos["x"], robot[i].pos["y"], robot[i].pos["z"],
                  robot[i].dir["x"], robot[i].dir["y"], robot[i].dir["z"],
                  length=robot[i].lenght, normalize=True, color=(r, g, b, 1))
        ax.text(robot[i].pos["x"], robot[i].pos["y"], robot[i].pos["z"], f'({(robot[i].pos["x"]):2.2f},'
                                                                         f' {(robot[i].pos["y"]):2.2f},'
                                                                         f' {(robot[i].pos["z"]):2.2f},'
                                                                         f' {(robot[i].theta):2.2f}[°])')

    ax.set_title('Zadanie proste kinematyki robota -> 3D')
    ax.set_xlabel('Oś X')
    ax.set_ylabel('Oś Y')
    ax.set_zlabel('Oś Z')
    plt.show()

def enterRobotRotations():
    Fivar = []

    for i in range(6):
        try:
            FiInput = math.radians(float(input(f"Podaj obrót w okół osi A{i + 1} (lub wpisz 'koniec' aby zakończyć): ")))
            if FiInput == 'koniec':
                break

            # Dodawanie danych do list
            Fivar.append(FiInput)

        except ValueError:
            print("Błędne dane. Wprowadź liczby.")
            Fivar.append(0)

    return Fivar

if __name__ == "__main__":
    # Wprowadzanie i rysowanie pierwszego zestawu danych
    theraVar = [0] * 6
    robot = robotKR8R2100HW

    drawindA3DChart(robot)

    # Aktualizowanie wykresu dla kolejnych zestawów danych
    while True:
        kontynuuj = input("Czy chcesz wprowadzić kolejne dane? (tak/nie): ").lower()
        if kontynuuj != 'tak':
            break

        theraVar = enterRobotRotations()
        for i in range(6):
            robot.update_axis_theta(i, robot[i].theta + theraVar[i])

        robot.get_total_transformation_matrix()

        for axis in robot:
            print(axis)

        drawindA3DChart(robot)
