import math
from random import randrange
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from RobotDefinition import robotKR8R2100HW
from RobotDefinition import Robot
import copy


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

    # Konfiguracja animacji ruchu
    t_stop = 2.5  # how many seconds to simulate
    history_len = 500  # how many trajectory points to display
    dt = 0.1
    t = np.arange(0, t_stop, dt)  # create a time array from 0..t_stop sampled at dt steps
    lines = [ax.plot([], [], [])[0] for _ in range(len(t))]


    np.set_printoptions(precision=6, suppress=True)
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

    transparetnDt = np.arange(0.1, 1, 0.9 / len(t))
    transparetnDt = list(map(lambda x: round(x, 3), transparetnDt))

    for i in range(len(robot)):
        r, g, b = randrange(0, 2), randrange(0, 2), randrange(0, 2),

        # for dt in range(len(t)):
        #     robotTrajectoryChaty = ax.quiver(robotTrajectory[dt][i].pos["x"], robotTrajectory[dt][i].pos["y"],
        #                                      robotTrajectory[dt][i].pos["z"],
        #                                      robotTrajectory[dt][i].dir["x"], robotTrajectory[dt][i].dir["y"],
        #                                      robotTrajectory[dt][i].dir["z"],
        #                                      length=robot[i].lenght, normalize=True, color=(r, g, b, transparetnDt[dt]))

        endPos = ax.quiver(robot[i].pos["x"], robot[i].pos["y"], robot[i].pos["z"],
                           robot[i].dir["x"], robot[i].dir["y"], robot[i].dir["z"],
                           length=robot[i].lenght, normalize=True, color=(r, g, b, 1))
        endText = ax.text(robot[i].pos["x"], robot[i].pos["y"], robot[i].pos["z"], f'({(robot[i].pos["x"]):2.2f},'
                                                                                   f' {(robot[i].pos["y"]):2.2f},'
                                                                                   f' {(robot[i].pos["z"]):2.2f},'
                                                                                   f' {math.degrees(robot[i].theta):2.2f}[°])')

    def animate(i, pos, dir):
        for line, pos in zip(dir, pos):
            # NOTE: there is no .set_data() for 3 dim data...

            line.set_data(pos[0, :i],pos[1, :i])
            line.set_3d_properties(pos[2, :i])
        return lines

    ani = animation.FuncAnimation(
        fig, animate, len(t), fargs=(robotTrajectoryMatrix, lines), interval=100)
    plt.show()


def enterRobotRotations():
    Fivar = []

    for i in range(6):
        try:
            FiInput = math.radians(
                float(input(f"Podaj obrót w okół osi A{i + 1} (lub wpisz 'koniec' aby zakończyć): ")))
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
    for axis in robot:
        print(axis)
    print(robot)
    drawindA3DChart(robot, theraVar)

    # Aktualizowanie wykresu dla kolejnych zestawów danych
    while True:
        kontynuuj = input("Czy chcesz wprowadzić kolejne dane? (tak/nie): ").lower()
        if kontynuuj != 'tak':
            break

        theraVar = enterRobotRotations()
        # robotStart = copy.deepcopy(robot)

        drawindA3DChart(robot, theraVar)
