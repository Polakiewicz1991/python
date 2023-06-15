class Test:
    # def __new__(cls):
    #     print("Hello class")

    #destruktor niszy obiekt na koniec programu
    def __del__(self):
        print("Bye class")

obj = Test()
obj2 = obj
lista = [obj2]
del obj
del obj2
del lista[0]
print("Koniec")