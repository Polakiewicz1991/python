import numpy as np
import math
from numpy import array as matrix
# from math import cos, sin
from math import pi as PI
from sympy import symbols, Eq, solve, sin, cos, trigsimp, simplify

a1, a2, a3, a4, a5, a6, a7, a8 = symbols('a1 a2 a3 a4 a5 a6 a7 a8')
Fi1, Fi2, Fi3, Fi4, Fi5, Fi6, Fi7, Fi8 = symbols('Fi1 Fi2 Fi3 Fi4 Fi5 Fi6 Fi7 Fi8')
d1, d2, d3, d4, d5, d6, d7, d8 = symbols('d1 d2 d3 d4 d5 d6 d7 d8')
alpha1, alpha2, alpha3, alpha4, alpha5, alpha6, alpha7, alpha8 = symbols('alpha1 alpha2 alpha3 alpha4 alpha5 alpha6 alpha7 alpha8')
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


def Ai(th= 0, d= 0, a= 0, alp= 0):
    return np.dot(np.dot(np.dot(rotZ(th),moveXYZ(z=d)),moveXYZ(x=a)),rotX(alp))


A1 = Ai(th=Fi1,d=d1,a=a1,alp=(alpha1))#np.dot(A10,A1)
A1  = matrix(list(map(lambda x: simplify(x), A1.flatten()))).reshape(A1.shape)
A1  = matrix(list(map(lambda x: trigsimp(x), A1.flatten()))).reshape(A1.shape)
print("A1")
print(f"X: {A1}")

Aresult = A1

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

