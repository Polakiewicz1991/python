class Solution:
    def swapPositions(self,lista, pos1, pos2):
        print("swapPositions lista: ", lista)
        print("swapPositions pos1: ", pos1)
        print("swapPositions pos2: ", pos2)
        lista[pos1], lista[pos2] = lista[pos2], lista[pos1]
        return lista

    def getPermutation2(self, n: int, k: int) -> str:

        lista = list(range(1,n+1))
        slownik = {1 : lista}
        silnia = 1
        silniaAux = 1

        for i in range(n,1,-1):
            silnia = silnia * i
            if i != n:
                silniaAux = silniaAux * i
        print("silnia: ", silnia)
        print("silniaAux: ", silniaAux)

        print("lista: ",lista)
        print("lista: ", self.swapPositions(lista,n-1,n-2))
        for i in range(silnia):
            j = i % n
            k = (i // n) % n
            print("i: ", i," j: ", j ," k: ", k)
            if i % n == 0:
                pass
            elif i % n == 1:
                # print("lista: ", swapPositions(lista, n - 1, n - 2))
                slownik[i] = self.swapPositions(lista, n - 1, n - 2)

    def getPermutation(self, n: int, k: int) -> str:

        # l = list(range(1,n+1))
        # print("l: ",l)
        # s = [str(integer) for integer in l]
        # lista = "".join(s)
        # print("lista: ", lista)
        # print("lista type: ", type(lista))
        #
        lista = list(range(1, n + 1))
        silnia = 1
        silniaAux = 1

        for i in range(n,1,-1):
            silnia = silnia * i
            if i != n:
                silniaAux = silniaAux * i

        wynikAux = [1, 2, 3, 4]
        wynik = []#[wynikAux for _ in range(silnia)]
        # wynik[0] = lista
        wynik.append(wynikAux)
        print("silnia: ", silnia)
        print("silniaAux: ", silniaAux)



        print("wynik: ", wynik)
        for i in range(1,silnia):
            j = n - (i % n) - 1
            k = n - ((i+1) % n) - 1
            print("i: ", i," j: ", j ," k: ", k)

            wynikAux = self.swapPositions(list(wynik[i-1]), j, k)
            print("wynikAux: ", wynikAux)
            wynik.append([wynikAux])




        print("wynik: ", wynik)
        # wynik.sort()
        print("wynik: ",wynik)

Wynik = Solution()
Wynik.getPermutation(4,0)