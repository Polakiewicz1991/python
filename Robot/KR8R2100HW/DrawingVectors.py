import math
from random import randrange
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from RobotDefinition import robotKR8R2100HW
import copy

def drawindA3DChart(robot,robotStart):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Ustawienia osi
    ax.set_title('Zadanie proste kinematyki robota -> 3D')
    ax.set_xlabel('Oś X')
    ax.set_ylabel('Oś Y')
    ax.set_zlabel('Oś Z')
    ax.set_xlim([-2200, 2200])
    ax.set_ylim([-2200, 2200])
    ax.set_zlim([-1000, 2200])

    # Konfiguracja animacji ruchu
    t_stop = 2.5  # how many seconds to simulate
    history_len = 500  # how many trajectory points to display
    dt = 0.1
    t = np.arange(0, t_stop, dt)  # create a time array from 0..t_stop sampled at dt steps

    dx, dy, dz = []*len(robot), []*len(robot), []*len(robot)
    dirx, diry, dirz = [] * len(robot), [] * len(robot), [] * len(robot)
    dtheta = [] * len(robot)

    #obliczanie animacji
    for i in range(len(robot)):
        dtheta.append(robotStart[i].theta + (((robot[i].theta - robotStart[i].theta) * t[:]) / t_stop))


        dx.append(robotStart[i].pos["x"] + (((robot[i].pos["x"] - robotStart[i].pos["x"]) * t[:]) / t_stop))
        dy.append(robotStart[i].pos["y"] + (((robot[i].pos["y"] - robotStart[i].pos["y"]) * t[:]) / t_stop))
        dz.append(robotStart[i].pos["z"] + (((robot[i].pos["z"] - robotStart[i].pos["z"]) * t[:]) / t_stop))
        dirx.append(robotStart[i].dir["x"] + (((robot[i].dir["x"] - robotStart[i].dir["x"]) * t[:]) / t_stop))
        diry.append(robotStart[i].dir["y"] + (((robot[i].dir["y"] - robotStart[i].dir["y"]) * t[:]) / t_stop))
        dirz.append(robotStart[i].dir["z"] + (((robot[i].dir["z"] - robotStart[i].dir["z"]) * t[:]) / t_stop))

    for i in range(len(robot)):
        r, g, b = randrange(0, 100) / 100, randrange(0, 100) / 100, randrange(0, 100) / 100,

        robotTrajectory = ax.quiver(dx[i], dy[i], dz[i],
                                    dirx[i], diry[i], dirz[i],
                                    length=robot[i].lenght, normalize=True, color=(r, g, b, 1))


        endPos = ax.quiver(robot[i].pos["x"], robot[i].pos["y"], robot[i].pos["z"],
                           robot[i].dir["x"], robot[i].dir["y"], robot[i].dir["z"],
                           length=robot[i].lenght, normalize=True, color=(r, g, b, 1))
        endText = ax.text(robot[i].pos["x"], robot[i].pos["y"], robot[i].pos["z"], f'({(robot[i].pos["x"]):2.2f},'
                                                                                     f' {(robot[i].pos["y"]):2.2f},'
                                                                                     f' {(robot[i].pos["z"]):2.2f},'
                                                                                     f' {(robot[i].theta):2.2f}[°])')


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

    drawindA3DChart(robot,robot)

    # Aktualizowanie wykresu dla kolejnych zestawów danych
    while True:
        kontynuuj = input("Czy chcesz wprowadzić kolejne dane? (tak/nie): ").lower()
        if kontynuuj != 'tak':
            break

        theraVar = enterRobotRotations()
        robotStart = copy.deepcopy(robot)

        print(id(robot))
        print(id(robotStart))

        for i in range(6):
            robot.update_axis_theta(i, robot[i].theta + theraVar[i])

        robot.get_total_transformation_matrix()

        drawindA3DChart(robot,robotStart)
