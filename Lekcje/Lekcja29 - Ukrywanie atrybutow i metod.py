class Test:
    # lista = [] - dostępne z zewnątrz
    __lista = [] # _przed nazwą zmiennych sprawia, że zmienna jest prywatna
    #__lista = [] - jeszcze bardziej zabezpiecza, można się odwołać z zewnątrz
    #poprzez dodanie nazwy klasy przed nazwą zmiennej _Test__lista
    def dodaj(self,arg):
        self.__lista.append(arg)

    def zdejmij(self):
        if len(self.__lista) > 0:
            return self.__lista.pop(len(self.__lista) - 1)
        else:
            return

obj = Test()

obj.dodaj("A")
obj.dodaj("B")
obj._Test__lista.append("x")
obj.dodaj("C")
print(obj.zdejmij())
print(obj._Test__lista)