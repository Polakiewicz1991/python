from random import  randint
class RandomizedSet:

    def __init__(self):
        self.lista = []
    def insert(self, val: int) -> bool:
        if val not in self.lista:
            self.lista.append(val)
            return True
        else:
            return False
    def remove(self, val: int) -> bool:
        if val in self.lista:
            self.lista.remove(val)
            return True
        else:
            return False
    def getRandom(self) -> int:
        return self.lista[randint(0,len(self.lista))]


Wynik = RandomizedSet()
boolResult = Wynik.insert(1)
print(boolResult)
print(Wynik.lista)
boolResult = Wynik.insert(1)
print(boolResult)
print(Wynik.lista)