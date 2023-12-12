import numpy as np
import math
from numpy import array as matrix
# from math import cos, sin
from math import pi as PI
from sympy import symbols, Eq, solve, sin, cos, trigsimp, simplify


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

#Pierwsza oś A1
A10 = Ai(th=0,d=3,a=0,alp=0)
Fi1 = math.radians(float(input("Podaj kąt A1 [°]: ")))#PI/4
A1 = rotZ(Fi1)
A1r = np.dot(A10,A1)

#Druga oś A2
A20 = Ai(th=0,d=0,a=3,alp=0)
A21 = Ai(th=(PI/2),d=0,a=2,alp=(PI/2))
A22 = Ai(th=(PI/2),d=0,a=1,alp=(0))
A2r = np.dot(np.dot(np.dot(A1r,A20),A21),A22)
Fi2 = math.radians(float(input("Podaj kąt A2 [°]: ")))
A2 = rotZ(Fi2)
A2r = np.dot(A2r,A2)

#Trzecia oś A3
A30 = Ai(th=(0),d=0,a=10,alp=0)
A3r = np.dot(A2r,A30)
Fi3= math.radians(float(input("Podaj kąt A3 [°]: ")))
A3 = rotZ(Fi3)
A3r = np.dot(A3r,A3)

#Czwarta oś A4
A40 = Ai(th=(PI/2),d=0,a=6,alp=(PI/2))
A4r = np.dot(A3r,A40)
Fi4= math.radians(float(input("Podaj kąt A4 [°]: ")))
A4 = rotZ(Fi4)
A4r = np.dot(A4r,A4)


#Piąta oś A5
A50 = Ai(th=(0),d=0,a=0,alp=(0))
A5r = np.dot(A4r,A50)
Fi5= math.radians(float(input("Podaj kąt A5 [°]: ")))
A5 = rotZ(Fi5)
A5r = np.dot(A5r,A5)

#Szósta oś A6
A60 = Ai(th=(0),d=0,a=2,alp=(0))
# A51 = Ai(th=(0),d=0,a=2,alp=(0))
# A41 = Ai(th=(PI/2),d=0,a=0,alp=(PI/2))
# A42 = Ai(th=(PI/2),d=0,a=0,alp=(0))
# A4r = np.dot(np.dot(np.dot(A3r,A40),A41),A42)


A6r  =np.dot(A5r,A60)
Fi6= math.radians(float(input("Podaj kąt A6 [°]: ")))
A6 = rotZ(Fi6)
A6r = np.dot(A6r,A6)







# # Upraszczenie za pomocą simplify
# simplified_expression  = matrix(list(map(lambda x: simplify(x), Aresult.flatten()))).reshape(Aresult.shape)
# # Upraszczenie za pomocą trigsimp -  jest bardziej ukierunkowana na upraszczanie wyrażeń trygonometrycznych
# simplified_expression  = matrix(list(map(lambda x: trigsimp(x), Aresult.flatten()))).reshape(Aresult.shape)
#
# print("Obiczone wyrażenie:")
# print(Aresult)
# print("\nUproszczone wyrażenie:")
# print(simplified_expression)
# print("\nWyniki dala XYZ:")
# print(f"X: {simplified_expression[0][3]}")
# print(f"Y: {simplified_expression[1][3]}")
# print(f"Z: {simplified_expression[2][3]}")

# calcX = simplified_expression[0][3]
# print(f"X: {calcX.evalf(subs={a1: 10, a2: 20, Fi1: 0, Fi2: 0})}")

colors = [(1, 0, 0, 1.0), (1, 0.5, 0, 1.0), (1, 1, 0, 1.0), (0, 1, 0, 1.0), (0.5, 0.5, 0, 1.0), (1, 0.5, 0, 1.0), (1, 0.5, 1, 1.0)]
x = [0, A1r[0][3], A2r[0][3], A3r[0][3], A4r[0][3], A5r[0][3], A6r[0][3]]
y = [0, A1r[1][3], A2r[1][3], A3r[1][3], A4r[1][3], A5r[1][3], A6r[1][3]]
z = [0, A1r[2][3], A2r[2][3], A3r[2][3], A4r[2][3], A5r[2][3], A6r[2][3]]

print(x)
print(y)
print(z)

# print(A1r)
# print(A2r)
# print(A3r)
# print(A4r)
# print(A5r)