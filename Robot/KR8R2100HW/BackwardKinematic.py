from scipy.optimize import fsolve
from sympy import symbols, Eq, nsolve
from RobotDefinition import Robot
import pickle
import numpy as np

"""
#Spróbujemy obliczyć wartości dla:
#[  0   0   1   1300]
#[  0   -1  0   0]
#[  1   0   0   1600]


[[  nx  sx  ax  dx]
[   ny  sy  ay  dy]
[   nz  sz  az  dz]
[   0   0   0   1]]

[0, 0, 1, 0, -1, 0, 1, 0, 0, 1300, 0, 1600]
from scipy.optimize import fsolve

# Definicja funkcji układu równań
def equations(vars):
    x1, x2, x3, x4, x5, x6 = vars
    # Tutaj wprowadź równania zgodnie z twoimi potrzebami
    eq1 = x1 + x2 + x3 - 3
    eq2 = x4 * x5 - x6 - 1
    # ...
    eq12 = x1 * x2 - x3 - 2

    return [eq1, eq2, ..., eq12]

# Początkowe przybliżenia dla zmiennych
initial_guess = [1, 1, 1, 1, 1, 1]

# Rozwiązanie układu równań nieliniowych
solution = fsolve(equations, initial_guess)

print("Rozwiązanie:", solution)


def equations(vars):
    theta1, theta2, theta3, theta4, theta5, theta6 = vars

    initPos = [0, 0, 1, 0, -1, 0, 1, 0, 0, 1300, 0, 1600]

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

    # return [nx, ny, nz, sx, sy, sz, ax, ay, az, dx, dy, dz]
    return [nx, sy, az, dx, dy, dz]

startPos = [robot[1].theta, robot[2].theta, robot[3].theta, robot[4].theta, robot[5].theta, robot[6].theta]
solution = fsolve(equations, startPos)

print("Rozwiązanie:", solution)
"""

# Konfiguracja wyświetlania danych w macierzy
np.set_printoptions(precision=6, suppress=True)

# Wprowadzanie i rysowanie pierwszego zestawu danych
robotKR8R2100HW = Robot

# odczytanie danych robota z pliku
with open('robotKR8R2100HW.pkl', 'rb') as file:
    robotKR8R2100HW = pickle.load(file)

print(f"Total matrix:")
print(robotKR8R2100HW.total_symbol_matrix)
print(f"\n")
def calc(robot):
    # Definicja zmiennych
    theta1, theta2, theta3, theta4, theta5, theta6 = symbols("theta1 theta2 theta3 theta4 theta5 theta6")

    # Definicja równań
    initPos = [0, 0, 1, 0, -1, 0, 1, 0, 0, 1300, 0, 1600]
    # initPos = [0, -1, 0, 1300, 0, 1600]
    robPos = [robot[1].theta, robot[2].theta, robot[3].theta, robot[4].theta, robot[5].theta, robot[6].theta]
    robPos = [1, -1, 1, 1275, 0, 1665]
    print(robPos)

    nx = Eq(robot.total_symbol_matrix[0][0], initPos[0])
    ny = Eq(robot.total_symbol_matrix[1][0], initPos[1])
    nz = Eq(robot.total_symbol_matrix[2][0], initPos[2])
    sx = Eq(robot.total_symbol_matrix[0][1], initPos[3])
    sy = Eq(robot.total_symbol_matrix[1][1], initPos[4])
    sz = Eq(robot.total_symbol_matrix[2][1], initPos[5])
    ax = Eq(robot.total_symbol_matrix[0][2], initPos[6])
    ay = Eq(robot.total_symbol_matrix[1][2], initPos[7])
    az = Eq(robot.total_symbol_matrix[2][2], initPos[8])
    dx = Eq(robot.total_symbol_matrix[0][3], initPos[9])
    dy = Eq(robot.total_symbol_matrix[1][3], initPos[10])
    dz = Eq(robot.total_symbol_matrix[2][3], initPos[11])

    # nx = robot.total_symbol_matrix[0][0] - initPos[0]
    # ny = robot.total_symbol_matrix[1][0] - initPos[1]
    # nz = robot.total_symbol_matrix[2][0] - initPos[2]
    # sx = robot.total_symbol_matrix[0][1] - initPos[3]
    # sy = robot.total_symbol_matrix[1][1] - initPos[4]
    # sz = robot.total_symbol_matrix[2][1] - initPos[5]
    # ax = robot.total_symbol_matrix[0][2] - initPos[6]
    # ay = robot.total_symbol_matrix[1][2] - initPos[7]
    # az = robot.total_symbol_matrix[2][2] - initPos[8]
    # dx = robot.total_symbol_matrix[0][3] - initPos[9]
    # dy = robot.total_symbol_matrix[1][3] - initPos[10]
    # dz = robot.total_symbol_matrix[2][3] - initPos[11]

    # nx = robot.total_symbol_matrix[0][0]
    # ny = robot.total_symbol_matrix[1][0]
    # nz = robot.total_symbol_matrix[2][0]
    # sx = robot.total_symbol_matrix[0][1]
    # sy = robot.total_symbol_matrix[1][1]
    # sz = robot.total_symbol_matrix[2][1]
    # ax = robot.total_symbol_matrix[0][2]
    # ay = robot.total_symbol_matrix[1][2]
    # az = robot.total_symbol_matrix[2][2]
    # dx = robot.total_symbol_matrix[0][3]
    # dy = robot.total_symbol_matrix[1][3]
    # dz = robot.total_symbol_matrix[2][3]

    # Lista równań
    # equations = [nx, ny, nz, sx, sy, sz, ax, ay, az, dx, dy, dz]
    equations = [nz, sy, ax, dx, dy, dz]

    # vars = robPos
    # dz.subs({theta1: vars[0], theta2: vars[1], theta3: vars[2], theta4: vars[3], theta5: vars[4], theta6: vars[5]})
    # print(dz.evalf())


    # Przekształć równania w funkcję liczbową
    # def equations_numeric(vars):
    #     print("vars", vars)
    #     return [equation.subs({theta1: vars[0], theta2: vars[1], theta3: vars[2], theta4: vars[3], theta5: vars[4], theta6: vars[5]}) for
    #             equation in equations]

    # Rozwiązanie układu równań

    solution = nsolve(equations, [theta1, theta2, theta3, theta4, theta5, theta6], robPos, prec=35)
    print(solution)
    # print("Rozwiązanie:", solution)

    # print(equations_numeric(robPos))

    # Użyj fsolve
    # numeric_solution = fsolve(equations_numeric, robPos)
    # print("Numeric Solution:", numeric_solution)


calc(robotKR8R2100HW)