from RobotDefinition import Robot

from numpy import pi

import pickle

# Tworzenie obiektu reprezentującego robota
robotKR8R2100HW = Robot()

robotKR8R2100HConstant = {"type": [1, 1, 1, 1, 1, 1],
                          "theta": [0, pi / 2, 0, 0, 0, 0],
                          "d": [520, 0, 0, 1015, 0, 100],
                          "a": [160, 980, 220, 0, 0, -50],
                          "alpha": [pi / 2, 0, pi / 2, -pi / 2, pi / 2, 0]}

# Dodawanie osi do robota
for i in range(6):
    robotKR8R2100HW.add_axis(type=robotKR8R2100HConstant["type"][i],
                             theta=robotKR8R2100HConstant["theta"][i],
                             d=robotKR8R2100HConstant["d"][i],
                             a=robotKR8R2100HConstant["a"][i],
                             alpha=robotKR8R2100HConstant["alpha"][i])



# Pobieranie macierzy transformacji dla całego robota
total_symbol_transformation_matrix = robotKR8R2100HW.get_symbol_transformation_matrix()
total_transformation_matrix = robotKR8R2100HW.get_total_transformation_matrix()

# Wyświetlanie macierzy transformacji
# print("Macierz transformacji dla całego robota:")
# print(total_transformation_matrix)

# for axis in robotKR8R2100HW.axes:
#     print(axis)

# print(f"Ilość osi robota {len(robotKR8R2100HW)}")

with open('robotKR8R2100HW.pkl', 'wb') as file:
    pickle.dump(robotKR8R2100HW, file)

with open('robotKR8R2100HW.pkl', 'rb') as file:
    robotKR8R2100HW = pickle.load(file)

print("Odczytane dane robota")
print(robotKR8R2100HW)

print("macierz total:")
print(robotKR8R2100HW.total_symbol_matrix)