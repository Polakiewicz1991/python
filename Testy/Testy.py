import numpy as np
# List of strings
l = ['sat', 'bat', 'cat', 'mat']


for x in zip(*l):
    print(x)

z = list(zip(*l))
y = tuple(zip(*l))
x = set(zip(*l))
print("z", z)
print("y", y)
print("x", x)


test = list(map(list, l))
print(test)

# String from list
testStr = ''
for x in test:
    testStr += ''.join(x) + ' '
print(testStr)

randomVar = np.random.random(3)
print(type(randomVar))
max_step=0.05
steps = np.random.uniform(-max_step, max_step, size=(30, 3))
print(np.random.random(3))
print(steps)

import numpy as np

# Przygotowanie danych
liczba_probek = 25  # Ilość próbek czasu
liczba_osi = 6  # Ilość osi

# Inicjalizacja tablicy dla każdej osi
robotTrajectory = np.empty((liczba_probek, liczba_osi, 3))

# Pętla po czasie (dt)
for dt in range(liczba_probek):
    # Pętla po osiach (i)
    for i in range(liczba_osi):
        # Przykładowe dane - możesz je dostosować do swoich potrzeb
        robotTrajectory[dt][i][0] = np.random.rand()  # Pozycja X
        robotTrajectory[dt][i][1] = np.random.rand()  # Pozycja Y
        robotTrajectory[dt][i][2] = np.random.rand()  # Pozycja Z

# Wyświetlenie przykładowych danych
print(robotTrajectory)