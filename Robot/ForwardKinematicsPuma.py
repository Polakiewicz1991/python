import numpy as np
import math
from numpy import array as matrix
# from math import cos, sin
from math import pi as PI
from sympy import symbols, Eq, solve, sin, cos, trigsimp, simplify

# a1, a2, a3, a4, a5, a6, a7, a8 = symbols('a1 a2 a3 a4 a5 a6 a7 a8')
# Fi1, Fi2, Fi3, Fi4, Fi5, Fi6, Fi7, Fi8 = symbols('Fi1 Fi2 Fi3 Fi4 Fi5 Fi6 Fi7 Fi8')
# d1, d2, d3, d4, d5, d6, d7, d8 = symbols('d1 d2 d3 d4 d5 d6 d7 d8')

def rotX(alpha):
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

def moveXYZ(x = 0, y = 0, z = 0):
    return matrix([ [1,                 0,                  0,              x],
                    [0,                 1,                  0,              y],
                    [0,                 0,                  1,              z],
                    [0,                 0,                  0,              1]])


alpha1, alpha2, alpha3, alpha4, alpha5, alpha6, alpha7, alpha8 = PI/2, 0, 0, PI/2, -PI/2, PI/2, 0, 0

a1 = 2#(int(input("Podaj odległość między osiami A1 - A2[mm]: ")))
d1 = 10#(int(input("Podaj przesunięcie między osiami A1 - A2[mm]: ")))
Fi1 = math.radians(float(input("Podaj kąt A1 [°]: ")))#PI/2#

Fi2 = PI/4#math.radians(float(input("Podaj kąt A2 [°]: ")))#PI/4

a3 = 10#(int(input("Podaj odległość między osiami A2 - A3[mm]: ")))

Fi4 = PI/4#math.radians(float(input("Podaj kąt A3 [°]: ")))#PI/4#-PI/4
a4 = 10#(int(input("Podaj odległość między osiami A3 - A4[mm]: ")))

d5 = 2#(int(input("Podaj przesunięcie między osiami A1 - A2[mm]: ")))

Fi5 = PI/4#math.radians(float(input("Podaj kąt A4 [°]: ")))#PI/4#-PI/4
Fi6 = PI/4#math.radians(float(input("Podaj kąt A5 [°]: ")))#PI/4#-PI/4

d7 = 2#(int(input("Podaj przesunięcie między osiami A1 - A2[mm]: ")))
Fi8 = PI/4#math.radians(float(input("Podaj kąt A6 [°]: ")))#PI/4#-PI/4
d8 = 2#(int(input("Podaj przesunięcie między osiami A1 - A2[mm]: ")))

A1 = np.dot(np.dot(rotZ(Fi1),moveXYZ(x=a1,z=d1)),rotX(alpha1))
A2 = rotZ(Fi2+(PI/2))
A3 = moveXYZ(x=a3)
A4 = np.dot(np.dot(rotZ(Fi4),moveXYZ(x=a4)),rotX(alpha4))
A5 = np.dot(moveXYZ(z= d5),rotX(alpha5))
A6 = np.dot(rotZ(Fi6),rotX(alpha6))
A7 = moveXYZ(z=d7)
A8 = np.dot(rotZ(Fi8),moveXYZ(z=d8))

A01 = A1
A12 = np.dot(A01,A2)
A23 = np.dot(A12,A3)
A34 = np.dot(A23,A4)
A45 = np.dot(A34,A5)
A56 = np.dot(A45,A6)
A67 = np.dot(A56,A7)
A78 = np.dot(A67,A8)

Aresult = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(A1,A2),A3),A4),A5),A6),A7),A8)
print("Aresult")
print(f"X: {Aresult[0][3]}")
print(f"Y: {Aresult[1][3]}")
print(f"Z: {Aresult[2][3]}")


# Upraszczenie za pomocą simplify
simplified_expression  = matrix(list(map(lambda x: simplify(x), Aresult.flatten()))).reshape(Aresult.shape)
# Upraszczenie za pomocą trigsimp -  jest bardziej ukierunkowana na upraszczanie wyrażeń trygonometrycznych
simplified_expression  = matrix(list(map(lambda x: trigsimp(x), Aresult.flatten()))).reshape(Aresult.shape)

print("Obiczone wyrażenie:")
print(Aresult)
print("\nUproszczone wyrażenie:")
print(simplified_expression)
print("\nWyniki dala XYZ:")
print(f"X: {simplified_expression[0][3]}")
print(f"Y: {simplified_expression[1][3]}")
print(f"Z: {simplified_expression[2][3]}")

# calcX = simplified_expression[0][3]
# print(f"X: {calcX.evalf(subs={a1: 10, a2: 20, Fi1: 0, Fi2: 0})}")

x0, y0, z0 = 0, 0, 0
x1, y1, z1 = A1[0][3], A1[1][3], A1[2][3]
x2, y2, z2 = A2[0][3], A2[1][3], A2[2][3]
x3, y3, z3 = A3[0][3], A3[1][3], A3[2][3]
x4, y4, z4 = A4[0][3], A4[1][3], A4[2][3]
x5, y5, z5 = A5[0][3], A5[1][3], A5[2][3]
x6, y6, z6 = A6[0][3], A6[1][3], A6[2][3]
x7, y7, z7 = A7[0][3], A7[1][3], A7[2][3]
x8, y8, z8 = A8[0][3], A8[1][3], A8[2][3]

# Atest = np.dot(moveXYZ(x=a1),moveXYZ(z=a3))
# print(Atest)
