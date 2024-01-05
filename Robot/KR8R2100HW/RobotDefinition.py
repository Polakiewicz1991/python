import math

import numpy as np
from numpy import array as matrix


from sympy import symbols, Eq, solve, trigsimp, simplify
from sympy import sin as sinSym
from sympy import cos as cosSym



class RobotAxis:
    def __init__(self, type, theta, d, a, alpha):
        """
        Dane osi:

        :param type: typ osi: 0 - nieruchoma, 1 - oś obrotowa, 2 - oś przesuwna
        :param theta: Obrót wokól osi Z
        :param d:  Odległość między osiami Z
        :param a: Odległość między osiami X
        :param alpha: Obrót wokół osi X
        """
        types = ["nieruchoma", "obrotowa", "przesuwna"]

        self.type = types[type]
        self.theta = theta
        self.d = d
        self.a = a
        self.alpha = alpha

        #Pozycja osi w przestrzeni kartezjańskiej
        self.pos = {"x": 0, "y": 0, "z": 0}
        self.dir = {"x": 0, "y": 0, "z": 0}
        self.lenght = 0

        #Macierze transformacji
        self.matrix_act = np.identity(4)
        self.matrix_to_base = np.identity(4)
        self.symbol_matrix_act = np.identity(4)
        self.symbol_matrix_to_base = np.identity(4)

    def get_transformation_matrix(self):
        """
        Funkcjie trygonometryczne niezbędne do obliczenia transformaty
        Zmienne prywatne
        """
        self.__ct = np.cos(self.theta)
        self.__st = np.sin(self.theta)
        self.__ca = np.cos(self.alpha)
        self.__sa = np.sin(self.alpha)

        """
        Oblicza macierz transformacji dla danej osi w notacji Denavita-Hartenberga.
        Uproszczona macierz transformacji, wynik rotZ * moveZ * moveX * rotX
        :return: Macierz transformacji 4x4
        """

        self.matrix_act = matrix([
            [self.__ct, -self.__st * self.__ca, self.__st * self.__sa, self.a * self.__ct],
            [self.__st, self.__ct * self.__ca, -self.__ct * self.__sa, self.a * self.__st],
            [0, self.__sa, self.__ca, self.d],
            [0, 0, 0, 1]])

        return self.matrix_act

    def get_transformation_symbol_matrix(self,thetaSymbol):
        """
        Funkcjie trygonometryczne niezbędne do obliczenia transformaty
        Zmienne prywatne
        """
        __ctSymbol = cosSym(thetaSymbol)
        __stSymbol = sinSym(thetaSymbol)
        __caSymbol = np.cos(self.alpha)
        __saSymbol = np.sin(self.alpha)

        """
        Oblicza macierz transformacji dla danej osi w notacji Denavita-Hartenberga.
        Uproszczona macierz transformacji, wynik rotZ * moveZ * moveX * rotX
        :return: Macierz transformacji 4x4
        """

        self.symbol_matrix_act = matrix([
            [__ctSymbol, -__stSymbol * __caSymbol, __stSymbol * __saSymbol, self.a * __ctSymbol],
            [__stSymbol, __ctSymbol * __caSymbol, -__ctSymbol * __saSymbol, self.a * __stSymbol],
            [0, __saSymbol, __caSymbol, self.d],
            [0, 0, 0, 1]])

        return self.symbol_matrix_act

    def rotX(self):
        """
        Rotacja wokół osi X
        """
        return matrix([[1, 0, 0, 0],
                       [0, self.__ca, -self.__sa, 0],
                       [0, self.__sa, self.__ca, 0],
                       [0, 0, 0, 1]])

    def rotY(self):
        """
        Rotacja wokół osi Y
        """
        return matrix([[self.__ca, 0, self.__sa, 0],
                       [0, 1, 0, 0],
                       [-self.__sa, 0, self.__ca, 0],
                       [0, 0, 0, 1]])

    def rotZ(self):
        """
        Rotacja wokół osi Z
        """
        return matrix([[self.__ca, -self.__sa, 0, 0],
                       [self.__sa, self.__ca, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])

    def moveXYZ(self, x=0, y=0, z=0):
        """
        Przesunięcie w osiach X i Z
        """
        return matrix([[1, 0, 0, self.a],
                       [0, 1, 0, 0],
                       [0, 0, 1, self.d],
                       [0, 0, 0, 1]])

    def update_theta(self, new_theta):
        """
        Aktualizuje wartość obrotu wokół osi theta.
        """
        self.theta = new_theta
        self.__ct = np.cos(self.theta)
        self.__st = np.sin(self.theta)


    def update_d(self, new_d):
        """
        Aktualizuje wartość odległości między osiami Z.
        """
        self.d = new_d

    def __str__(self):
        return (f"Oś {self.type}, "
               f"Obrót względem osi Z: {math.degrees(self.theta)} [°]\n"
               f"Odległość między osiami Z: {self.d} [mm]\n"
               f"Odległość między osiami X: {self.a} [mm]\n"
               f"Obrót względem osi X: {math.degrees(self.alpha)} [°]\n"
               f"Pozycja osi względem początku ukł. wsp.:\n"
               f"\tx:{(self.pos['x']):2.2f}\tdir x:{(self.dir['x']):2.2f},\n"
               f"\ty:{(self.pos['y']):2.2f}\tdir y:{(self.dir['y']):2.2f},\n"
               f"\tz:{(self.pos['z']):2.2f}\tdir z:{(self.dir['z']):2.2f},\n"
               f"\tdługość wektora:{(self.lenght):2.2f}")


class Robot:
    def __init__(self):
        self.axes = [RobotAxis(0,0,0,0,0)]
        self.total_matrix = np.identity(4)
        self.total_symbol_matrix = np.identity(4)

    def __len__(self):
        return len(self.axes)

    def __getitem__(self, index):
        return self.axes[index]

    def __str__(self):

        strReturn = f"Ilość osi robota {len(self)},\n"
        for axis in enumerate(self.axes):
            strReturn = strReturn + f"Obrót wokół osi A{axis[0]+1} = {math.degrees(axis[1].theta):2.2f}[°],\n"

        strReturn += f"Położenie flanszy robota: x:{(self.axes[len(self.axes) - 1].pos['x']):2.2f}, " \
                     f"y:{(self.axes[len(self.axes) - 1].pos['y']):2.2f}, " \
                     f"z:{(self.axes[len(self.axes) - 1].pos['y']):2.2f}, "

        return strReturn

    def add_axis(self, type, theta, d, a, alpha):
        """
        Dodaje oś do robota.
        """
        axis = RobotAxis(type, theta, d, a, alpha)
        self.axes.append(axis)

    def update_axis_theta(self, axis_index, new_theta):
        """
        Aktualizuje wartość obrotu wokół osi theta dla konkretnej osi.
        """
        if 0 <= axis_index < len(self.axes):
            self.axes[axis_index].update_theta(new_theta)

    def update_axis_d(self, axis_index, new_d):
        """
        Aktualizuje wartość odległości między osiami Z dla konkretnej osi.
        """
        if 0 <= axis_index < len(self.axes):
            self.axes[axis_index].update_d(new_d)

    def get_total_transformation_matrix(self):
        """
        Oblicza macierz transformacji dla całego robota na podstawie transformacji poszczególnych osi.
        :return: Macierz transformacji 4x4
        """

        self.total_matrix = np.identity(4)

        for axis in self.axes:
            self.total_matrix = np.dot(self.total_matrix, axis.get_transformation_matrix())

            axis.pos['x'] = self.total_matrix[0][3]
            axis.pos['y'] = self.total_matrix[1][3]
            axis.pos['z'] = self.total_matrix[2][3]

            axis.matrix_to_base = self.total_matrix

        if len(self) > 1:
            for i in range(len(self) - 1):
                self[i].dir['x'] = self[i + 1].pos['x'] - self[i].pos['x']
                self[i].dir['y'] = self[i + 1].pos['y'] - self[i].pos['y']
                self[i].dir['z'] = self[i + 1].pos['z'] - self[i].pos['z']
                self[i].lenght = (math.sqrt(((self[i].dir['x']) ** 2) + ((self[i].dir['y']) ** 2) + ((self[i].dir['z']) ** 2)))

        return self.total_matrix

    def get_symbol_transformation_matrix(self):
        """
        Oblicza symbolicznej macierz transformacji dla całego robota na podstawie transformacji poszczególnych osi.
        :return: Macierz transformacji 4x4
        """
        symbols_list = [symbols(f'theta{i}') for i in range(len(self))]

        print(symbols_list)

        for i, axis in enumerate(self.axes):
            axis.get_transformation_symbol_matrix(symbols_list[i])
            # TUTAJ ZMIENIAĆ JEŻELI CHCEMY OBLICZYĆ MACIEŻ CAŁEGO ROBOTA
            self.total_symbol_matrix = np.dot(self.total_symbol_matrix, axis.get_transformation_symbol_matrix(symbols_list[i]))
            # total_symbol_transformation_matrix = axis.get_transformation_symbol_matrix(symbols_list[i])

            self.total_symbol_matrix = matrix(list(map(lambda x: simplify(x), self.total_symbol_matrix.flatten()))).reshape(self.total_symbol_matrix.shape)
            self.total_symbol_matrix = matrix(list(map(lambda x: trigsimp(x), self.total_symbol_matrix.flatten()))).reshape(self.total_symbol_matrix.shape)
            if i == 0:
                self.total_symbol_matrix = matrix(list(map(lambda x: x.evalf(subs={symbols_list[0]: self.axes[i].theta}), self.total_symbol_matrix.flatten()))).reshape(self.total_symbol_matrix.shape)

            #Przypisanie macierzy opisującej położenie i oriętacje osi w przestrzeni
            axis.symbol_matrix_to_base = self.total_symbol_matrix

            print(f"oś {i}")
            print(axis.get_transformation_symbol_matrix(symbols_list[i]))
            print(f"oś suma {i}")
            print(self.total_symbol_matrix)

        return self.total_symbol_matrix
