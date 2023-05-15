
def funkcja_test(): #nagłówek funkcji
    print("Funkcja!")

funkcja_test()

def dodaj(x,y):
    print(x + 1)
    print(y + 2)

dodaj(1,2)


def dodaj(x,y):
    print(x + y)
    print(y + 2)

dodaj(3,3)

def dodaj(x,y = 1,z = 0):
    return x + y + z

dodaj(3, 3)
print(dodaj(3))
print("test")
print(dodaj("kupa"))

