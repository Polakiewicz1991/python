import numpy as np
import math
from numpy import array as matrix
# from math import cos, sin
from math import pi as PI
from sympy import symbols, Eq, solve, sin, cos, trigsimp, simplify

a1, a2, a3, a4, a5, a6, a7, a8 = symbols('a1 a2 a3 a4 a5 a6 a7 a8')
Fi1, Fi2, Fi3, Fi4, Fi5, Fi6, Fi7, Fi8 = symbols('Fi1 Fi2 Fi3 Fi4 Fi5 Fi6 Fi7 Fi8')
d1, d2, d3, d4, d5, d6, d7, d8 = symbols('d1 d2 d3 d4 d5 d6 d7 d8')
alpha1, alpha2, alpha3, alpha4, alpha5, alpha6, alpha7, alpha8 = PI/2, 0, 0, PI/2, -PI/2, PI/2, 0, 0
def rotX(alpha):
    return matrix([ [1,                 0,                  0,              0],
                    [0,                 cos(alpha),         -sin(alpha),    0],
                    [0,                 sin(alpha),         cos(alpha),     0],
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




A1 = np.dot(np.dot(rotZ(Fi1),moveXYZ(x=a1,z=d1)),rotX(alpha1))
A1  = matrix(list(map(lambda x: simplify(x), A1.flatten()))).reshape(A1.shape)
A1  = matrix(list(map(lambda x: trigsimp(x), A1.flatten()))).reshape(A1.shape)
print("A1")
print(f"X: {A1}")
# print(f"X: {A1[0][3]}")
# print(f"Y: {A1[1][3]}")
# print(f"Z: {A1[2][3]}")

A2 = rotZ(Fi2+(PI/2))
A2  = matrix(list(map(lambda x: simplify(x), A2.flatten()))).reshape(A2.shape)
A2  = matrix(list(map(lambda x: trigsimp(x), A2.flatten()))).reshape(A2.shape)
print("A2")
print(f"X: {A2}")
# print(f"X: {A2[0][3]}")
# print(f"Y: {A2[1][3]}")
# print(f"Z: {A2[2][3]}")
Aresult = np.dot(A1,A2)

A3 = moveXYZ(x=a3)
print("A3")
print(f"X: {A3}")
# print(f"X: {A3[0][3]}")
# print(f"Y: {A3[1][3]}")
# print(f"Z: {A3[2][3]}")
Aresult = np.dot(Aresult,A3)

A4 = np.dot(np.dot(rotZ(Fi4),moveXYZ(x=a4)),rotX(alpha4))
print("A4")
print(f"X: {A4}")
# print(f"X: {A4[0][3]}")
# print(f"Y: {A4[1][3]}")
# print(f"Z: {A4[2][3]}")
Aresult = np.dot(Aresult,A4)

A5 = np.dot(moveXYZ(z= d5),rotX(alpha5))
print("A5")
print(f"X: {A5}")
# print(f"X: {A5[0][3]}")
# print(f"Y: {A5[1][3]}")
# print(f"Z: {A5[2][3]}")
Aresult = np.dot(Aresult,A5)

A6 = np.dot(rotZ(Fi5),rotX(alpha6))
print("A6")
print(f"X: {A6}")
# print(f"X: {A6[0][3]}")
# print(f"Y: {A6[1][3]}")
# print(f"Z: {A6[2][3]}")
Aresult = np.dot(Aresult,A6)

A7 = moveXYZ(z=d7)
print("A7")
print(f"X: {A7}")
# print(f"X: {A7[0][3]}")
# print(f"Y: {A7[1][3]}")
# print(f"Z: {A7[2][3]}")
Aresult = np.dot(Aresult,A7)

A8 = np.dot(rotZ(Fi8),moveXYZ(z=d8))
print("A8")
print(f"X: {A8}")
# print(f"X: {A8[0][3]}")
# print(f"Y: {A8[1][3]}")
# print(f"Z: {A8[2][3]}")
Aresult = np.dot(Aresult,A8)

# Aresult = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(A1,A2),A3),A4),A5),A6),A7),A8)
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

calcX = simplified_expression[0][3]
print(f"X: {calcX.evalf(subs={a1: 10, a2: 20, Fi1: 0, Fi2: 0})}")

x0, y0, z0 = 0, 0, 0
x1, y1, z1 = A1[0][3], A1[1][3], A1[2][3]
x2, y2, z2 = A2[0][3], A2[1][3], A2[2][3]

print(simplified_expression[:][3])

Atest = np.dot(moveXYZ(x=a1),moveXYZ(z=a3))
print(Atest)
