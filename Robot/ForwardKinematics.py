import numpy as np
import math
from numpy import array as matrix
from math import cos, sin
from math import pi as PI
from sympy import symbols, Eq, solve

def rotXsymbol(alpha):
    return matrix([ [cos(alpha),        -sin(alpha),        0,              0],
                    [sin(alpha),        cos(alpha),         0,              0],
                    [0,                 0,                  1,              0],
                    [0,                 0,                  0,              1]])
def rotZ(alpha):
    return matrix([ [cos(alpha),        -sin(alpha),        0,              0],
                    [sin(alpha),        cos(alpha),         0,              0],
                    [0,                 0,                  1,              0],
                    [0,                 0,                  0,              1]])

def rotY(alpha):
    return matrix([ [cos(alpha),        0,                  sin(alpha),     0],
                    [0,                 1,                  0,              0],
                    [-sin(alpha),       0,                  cos(alpha),     0],
                    [0,                 0,                  0,              1]])

def rotX(alpha):
    return matrix([ [1,                 0,                  0,              0],
                    [0,                 cos(alpha),         -sin(alpha),    0],
                    [0,                 sin(alpha),         cos(alpha),     0],
                    [0,                 0,                  0,              1]])


def moveXYZ(x = 0, y = 0, z = 0):
    return matrix([ [1,                 0,                  0,              x],
                    [0,                 1,                  0,              y],
                    [0,                 0,                  1,              z],
                    [0,                 0,                  0,              1]])



a1 = (int(input("Długość ramienia A1 [°]: ")))#PI/4
Fivar1 = math.radians(int(input("Podaj kąt A1 [°]: ")))#PI/4
a2 = (int(input("Długość ramienia A2 [°]: ")))#PI/4
Fivar2 = math.radians(int(input("Podaj kąt A2 [°]: ")))#PI/4#-PI/4

A1 = np.dot(rotZ(Fivar1),moveXYZ(x=a1))
A2 = np.dot(rotZ(Fivar2),moveXYZ(x=a2))
Aresult = np.dot(A1,A2)

print(Aresult)
rounded_matrix = matrix(list(map(lambda x: round(x, 5), Aresult.flatten()))).reshape(Aresult.shape)
print("Wynik \n")
print(rounded_matrix)
print(f"X: {rounded_matrix[0][3]}, Y: {rounded_matrix[1][3]}, Z: {rounded_matrix[2][3]}, ")

x0, y0, z0 = 0, 0, 0
x1, y1, z1 = A1[0][3], A1[1][3], A1[2][3]
x2, y2, z2 = A2[0][3], A2[1][3], A2[2][3]
