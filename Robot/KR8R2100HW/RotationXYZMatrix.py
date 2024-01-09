import numpy as np
from numpy import array as matrix

from sympy import symbols, Eq, solve, sin, cos, trigsimp, simplify

import pickle

alpha, beta, gamma = symbols('alpha beta gamma')

def rotX(gamma):
    return matrix([ [1,                 0,                  0,              0],
                    [0,                 cos(gamma),         -sin(gamma),    0],
                    [0,                 sin(gamma),         cos(gamma),     0],
                    [0,                 0,                  0,              1]])


def rotY(beta):
    return matrix([ [cos(beta),         0,                  sin(beta),      0],
                    [0,                 1,                  0,              0],
                    [-sin(beta),        0,                  cos(beta),      0],
                    [0,                 0,                  0,              1]])


def rotZ(alpha):
    return matrix([ [cos(alpha),        -sin(alpha),        0,              0],
                    [sin(alpha),        cos(alpha),         0,              0],
                    [0,                 0,                  1,              0],
                    [0,                 0,                  0,              1]])


def moveXYZ(x = 0, y = 0, z = 0):
    return matrix([ [1,                 0,                  0,              x],
                    [0,                 1,                  0,              y],
                    [0,                 0,                  1,              z],
                    [0,                 0,                  0,              1]])


# Nazwy obrotów jak w KUKA
# alpha - obrót w okół Z, beta - obrót w okół Y, gamma - obrót w okół X
Rx = rotX(gamma)
Ry = rotY(beta)
Rz = rotZ(alpha)

Rtotal = np.dot(np.dot(Rx,Ry),Rz)
Rrot = Rtotal[:3, :3]
print("Rrot:", Rrot, "\n")

with open('Rrot.pkl', 'wb') as file:
    pickle.dump(Rrot, file)

with open('Rrot.pkl', 'rb') as file:
    Rrot = pickle.load(file)

print("Odczytane dane rotacji")
print(Rrot)



