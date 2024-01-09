import math

from scipy.optimize import fsolve

from sympy import symbols, Eq, nsolve

from RobotDefinition import Robot

import pickle

import numpy as np


from numpy import array as matrix
# Konfiguracja wyświetlania danych w macierzy
np.set_printoptions(precision=6, suppress=True)

# Wprowadzanie i rysowanie pierwszego zestawu danych
robotKR8R2100HW = Robot
# Rrot = matrix[4,4]

# odczytanie danych robota z pliku
with open('robotKR8R2100HW.pkl', 'rb') as file:
    robotKR8R2100HW = pickle.load(file)
with open('Rrot.pkl', 'rb') as file:
    Rrot = pickle.load(file)

print(f"Total matrix:")
print(robotKR8R2100HW.total_symbol_matrix)
print(robotKR8R2100HW.total_matrix)
print(f"\n")

print(f"Matrix rotacji:")
print(Rrot)
print(f"\n")

def calc(robot,initPos):
    # Definicja zmiennych
    theta1, theta2, theta3, theta4, theta5, theta6 = symbols("theta1 theta2 theta3 theta4 theta5 theta6")
    alpha, beta, gamma = symbols('alpha beta gamma')

    # Pozycja robota
    robPos = [robot[1].theta, robot[2].theta, robot[3].theta, robot[4].theta, robot[5].theta, robot[6].theta]
    print("robPos: ", robPos)

    #Orientacje robota
    vectorX = robot.total_matrix[:3, 0]
    vectorY = robot.total_matrix[:3, 1]
    vectorZ = robot.total_matrix[:3, 2]
    print("vectorX: ", vectorX)
    print("vectorY: ", vectorY)
    print("vectorZ: ", vectorZ)

    # Wypisanie równań macierzy orientacji
    Rnx = Rrot[0][0] - initPos[0]
    Rny = Rrot[1][0] - initPos[1]
    Rnz = Rrot[2][0] - initPos[2]
    Rsx = Rrot[0][1] - initPos[3]
    Rsy = Rrot[1][1] - initPos[4]
    Rsz = Rrot[2][1] - initPos[5]
    Rax = Rrot[0][2] - initPos[6]
    Ray = Rrot[1][2] - initPos[7]
    Raz = Rrot[2][2] - initPos[8]

    # Lista równań pozycji
    equations_rot_X = [Rnx, Rny, Rnz]
    equations_rot_Y = [Rsx, Rsy, Rsz]
    equations_rot_Z = [Rax, Ray, Raz]
    equations_rot = [Rnx, Rsy, Raz]

    # Wypisanie równań macierzy robota
    nx = robot.total_symbol_matrix[0][0] - initPos[0]
    ny = robot.total_symbol_matrix[1][0] - initPos[1]
    nz = robot.total_symbol_matrix[2][0] - initPos[2]
    sx = robot.total_symbol_matrix[0][1] - initPos[3]
    sy = robot.total_symbol_matrix[1][1] - initPos[4]
    sz = robot.total_symbol_matrix[2][1] - initPos[5]
    ax = robot.total_symbol_matrix[0][2] - initPos[6]
    ay = robot.total_symbol_matrix[1][2] - initPos[7]
    az = robot.total_symbol_matrix[2][2] - initPos[8]
    dx = robot.total_symbol_matrix[0][3] - initPos[9]
    dy = robot.total_symbol_matrix[1][3] - initPos[10]
    dz = robot.total_symbol_matrix[2][3] - initPos[11]

    # Lista równań pozycji
    equations_robot = [nz, sy, ax, dx, dy, dz]

    # Przekształć równania w funkcję liczbową
    def equations_numeric_robot_pos(vars):
        return [equation.evalf(subs={theta1: vars[0], theta2: vars[1], theta3: vars[2], theta4: vars[3], theta5: vars[4], theta6: vars[5]}) for
                equation in equations_robot]
    def equations_numeric_rotation_X(vars):
        return [equation.evalf(subs={alpha: vars[0], beta: vars[1], gamma: vars[2]}) for
                equation in equations_rot_X]
    def equations_numeric_rotation_Y(vars):
        return [equation.evalf(subs={alpha: vars[0], beta: vars[1], gamma: vars[2]}) for
                equation in equations_rot_Y]
    def equations_numeric_rotation_Z(vars):
        return [equation.evalf(subs={alpha: vars[0], beta: vars[1], gamma: vars[2]}) for
                equation in equations_rot_Z]

    def equations_numeric_rotation(vars):
        return [equation.evalf(subs={alpha: vars[0], beta: vars[1], gamma: vars[2]}) for
                equation in equations_rot]

    # print("equations_numeric_robot_pos(robPos): ",equations_numeric_robot_pos(robPos))
    #
    # # Użyj fsolve
    # numeric_solution = fsolve(equations_numeric_robot_pos, robPos)
    # print("Numeric Solution robot pos:", numeric_solution)
    #
    # for i,num in enumerate(numeric_solution):
    #     calc = math.degrees(num-robPos[i])%360
    #     if calc > 180:
    #         calc -= 360
    #     print(f"theta{i+1}: ", calc)

    # Określenie ograniczeń (limity)
    lower_bounds = [-math.pi, -math.pi, -math.pi]  # dolne limity
    upper_bounds = [math.pi, math.pi, math.pi]  # górne limity
    numeric_solution = fsolve(equations_numeric_rotation_X, vectorX, factor=(0.005))
    print("Numeric Solution vector X:", numeric_solution)
    for angle in numeric_solution:
        print("Kąt:",math.degrees(angle))
    numeric_solution = fsolve(equations_numeric_rotation_Y, vectorY, factor=(0.005))
    print("Numeric Solution vector Y:", numeric_solution)
    for angle in numeric_solution:
        print("Kąt:",math.degrees(angle))
    numeric_solution = fsolve(equations_numeric_rotation_Z, vectorZ, factor=(0.005))
    print("Numeric Solution vector Z:", numeric_solution)
    for angle in numeric_solution:
        print("Kąt:",math.degrees(angle))
    numeric_solution = fsolve(equations_numeric_rotation, vectorZ, factor=(0.005))
    print("Numeric Solution vector diagonal:", numeric_solution)
    for angle in numeric_solution:
        print("Kąt:",math.degrees(angle))

    print(Rrot[0][2].evalf(subs={alpha: numeric_solution[0], beta: numeric_solution[1], gamma: numeric_solution[2]}))
    print(Rrot[1][2].evalf(subs={alpha: numeric_solution[0], beta: numeric_solution[1], gamma: numeric_solution[2]}))
    print(Rrot[2][2].evalf(subs={alpha: numeric_solution[0], beta: numeric_solution[1], gamma: numeric_solution[2]}))

initPos = [0, 0, 1, 0, -1, 0, 1, 0, 0, 1300, 0, 1600]
initPos = [1, 0, 0, 0, 1, 0, 0, 0, 1, 1300, 0, 1600]
calc(robotKR8R2100HW,initPos)