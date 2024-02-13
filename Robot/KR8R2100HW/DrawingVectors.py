import pickle

import math
from random import randrange

import numpy as np
from numpy import array as matrix

import matplotlib.pyplot as plt
import matplotlib.animation as animation


# from RobotDefinition import robotKR8R2100HW
from RobotDefinition import Robot
import copy

from PositionCalculation import pointTCP, robMatrix
from PositionCalculation import theta1, theta2, theta3, theta4, theta5, theta6


def drawindA3DChart(robot, theraVar):
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

    #Narysowanie wektorów osi układu kartezjaństego
    ax.text(2200, 0, 0, 'X+')
    ax.quiver(1,0,0,1,0,0,length=2200, normalize=True, color=(0, 0, 0, 0.1))
    ax.text(0, 2200, 0, 'Y+')
    ax.quiver(0,1,0,0,1,0,length=2200, normalize=True, color=(0, 0, 0, 0.1))
    ax.text(0, 0, 2200, 'Z+')
    ax.quiver(0,0,1,0,0,1,length=2200, normalize=True, color=(0, 0, 0, 0.1))

    # Konfiguracja animacji ruchu
    t_stop = 2.5  # how many seconds to simulate
    history_len = 500  # how many trajectory points to display
    dt = 0.1
    t = np.arange(0, t_stop, dt)  # create a time array from 0..t_stop sampled at dt steps
    lines = [ax.quiver([], [], [], [], [], []) for _ in range(len(t))]
    transparetnDt = (np.linspace(dt, 1, len(t)))
    transparetnDt = list(map(lambda _ : _**2,transparetnDt))

    # Inicjalizacja macierzy
    dtheta = [] * len(robot)
    robotTrajectory = [Robot] * len(t)
    robotTrajectoryMatrix = np.empty((len(robot), 3, len(t)))
    robotTrajectoryDirMatrix = np.empty((len(robot), 3, len(t)))

    # Różniczkowanie zmiany kąta robota
    for i in range(len(robot)):
        dtheta.append(robot[i].theta + ((theraVar[i] * t[:]) / t_stop))

    # U torzenie trajektoru ruchu robota
    for dt in range(len(t)):
        robotTrajectory[dt] = copy.deepcopy(robot)
        for i in range(len(dtheta)):
            robotTrajectory[dt].update_axis_theta(axis_index=i, new_theta=dtheta[i][dt])
            robotTrajectory[dt].get_total_transformation_matrix()

            robotTrajectoryMatrix[i][0][dt] = robotTrajectory[dt][i].pos['x']  # Pozycja X
            robotTrajectoryMatrix[i][1][dt] = robotTrajectory[dt][i].pos['y']  # Pozycja Y
            robotTrajectoryMatrix[i][2][dt] = robotTrajectory[dt][i].pos['z']  # Pozycja Z

            robotTrajectoryDirMatrix[i][0][dt] = robotTrajectory[dt][i].dir['x']  # Pozycja X
            robotTrajectoryDirMatrix[i][1][dt] = robotTrajectory[dt][i].dir['y']  # Pozycja Y
            robotTrajectoryDirMatrix[i][2][dt] = robotTrajectory[dt][i].dir['z']  # Pozycja Z

    # Aktualizaja osi robota
    for i in range(len(robot)):
        robot.update_axis_theta(axis_index=i, new_theta=robot[i].theta + theraVar[i])
    robot.get_total_transformation_matrix()

    for i in range(len(robot)):
        ax.quiver(robot[i].pos["x"], robot[i].pos["y"], robot[i].pos["z"],
                  robot[i].dir["x"], robot[i].dir["y"], robot[i].dir["z"],
                  length=robot[i].lenght, normalize=True, color=(r[i], g[i], b[i], 1))

        """
        Zakomentowane wyświtlanie położenia każdej osi robota w przestrzeni w raz z kątem robota w tej przestrzeni
        
        endText = ax.text(robot[i].pos["x"], robot[i].pos["y"], robot[i].pos["z"], f'({(robot[i].pos["x"]):2.2f},'
                                                                                   f' {(robot[i].pos["y"]):2.2f},'
                                                                                   f' {(robot[i].pos["z"]):2.2f},'
                                                                                   f' {math.degrees(robot[i].theta):2.2f}[°])')
        """

    #Opis położenia punktu TCP robota
    j = len(robot) - 1
    ax.text(robot[j].pos["x"], robot[j].pos["y"], robot[j].pos["z"], f'({(robot[j].pos["x"]):2.2f},'
                                                                               f' {(robot[j].pos["y"]):2.2f},'
                                                                               f' {(robot[j].pos["z"]):2.2f},'
                                                                               f' {math.degrees(robot[j].theta):2.2f}[°])')

    def animate(i, pos, dir, lines):
        for j, (line, pos, dir) in enumerate(zip(lines, pos, dir)):

            line = ax.quiver(pos[0,i], pos[1,i], pos[2,i], dir[0,i], dir[1,i], dir[2,i],  color=(r[j], g[j], b[j], transparetnDt[i]))
        return lines

    ani = animation.FuncAnimation(
        fig, animate, len(t), fargs=(robotTrajectoryMatrix, robotTrajectoryDirMatrix, lines), interval=100, repeat=False)

    plt.show()

def calcRobotData(robot, theraVar):
    resultTCP = [_.evalf(
        subs={theta1: robot[1].theta, theta2: robot[2].theta, theta3: robot[3].theta,
              theta4: robot[4].theta, theta5: robot[5].theta, theta6: robot[6].theta})
        for _ in pointTCP]

    print("resultTCP", resultTCP)

    resultMatrix = np.zeros((4,4))
    for i,line in enumerate(robot.total_symbol_matrix):
        for j, cell in enumerate(line):
            if (not isinstance(robot.total_symbol_matrix[i][j], int) or not isinstance(robot.total_symbol_matrix[i][j], float)):
                resultMatrix[i][j] = robot.total_symbol_matrix[i][j].evalf(
                    subs={theta1: robot[1].theta, theta2: robot[2].theta, theta3: robot[3].theta,
                          theta4: robot[4].theta, theta5: robot[5].theta, theta6: robot[6].theta})

            else:
                resultMatrix[i][j] = robot.total_symbol_matrix[i][j]

            # if resultMatrix[i][j] > -1.0e-10 and resultMatrix[i][j] < 1.0e-10:
            #     resultMatrix[i][j] = 0

    print(f"resultMatrix:\n", resultMatrix)


def enterRobotRotations(robot):
    Fivar = []

    for i in range(len(robotKR8R2100HW)):
        if robotKR8R2100HW[i].type == "obrotowa":
            try:
                FiInput = math.radians(
                    float(input(f"Podaj obrót w okół osi A{i}, aktualna pozycja {math.degrees(robot[i].theta)}° (lub wpisz 'koniec' aby zakończyć): ")))
                if FiInput == 'koniec':
                    break

                # Dodawanie danych do list
                Fivar.append(FiInput)

            except ValueError:
                print("Błędne dane. Wprowadź liczby.")
                Fivar.append(0)
        else:
            Fivar.append(0)
    return Fivar


if __name__ == "__main__":
    # Konfiguracja wyświetlania danych w macierzy
    np.set_printoptions(precision=6, suppress=True)

    # Wprowadzanie i rysowanie pierwszego zestawu danych
    robotKR8R2100HW = Robot

    #odczytanie danych robota z pliku
    with open('robotKR8R2100HW.pkl', 'rb') as file:
        robotKR8R2100HW = pickle.load(file)

    print(f"Total matrix:\n")
    print(robotKR8R2100HW.total_symbol_matrix)
    print(f"\n")

    theraVar = [0] * len(robotKR8R2100HW)

    # r, g, b = [randrange(0, 2) for _ in range(len(robotKR8R2100HW))], [randrange(0, 2) for _ in range(len(robotKR8R2100HW))], [randrange(0, 2) for _ in range(len(robotKR8R2100HW))]
    r, g, b = [[0.5,1,1,0,1,0,0],
               [1,1,0,1,0.5,0,1],
               [0.5,0.5,1,1,0.5,1,0]]

    print(robotKR8R2100HW)

    calcRobotData(robotKR8R2100HW, theraVar)
    drawindA3DChart(robotKR8R2100HW, theraVar)

    # Aktualizowanie wykresu dla kolejnych zestawów danych
    while True:
        kontynuuj = input("Czy chcesz wprowadzić kolejne dane? (y): ").lower()
        if kontynuuj != 'y':
            break

        theraVar = enterRobotRotations(robotKR8R2100HW)

        calcRobotData(robotKR8R2100HW, theraVar)
        drawindA3DChart(robotKR8R2100HW, theraVar)
