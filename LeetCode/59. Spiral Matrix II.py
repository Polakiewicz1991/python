class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:

        auxlista = []#[0] * n
        listaResult = []

        # for i in range(n):
        #     listaResult.append(auxlista)

        for i in range(n ** 2):
            auxlista += [0]
            # print("auxlista: ", auxlista)
            # print("i+1 % {0}: ".format(n), ((i + 1) % n))
            if ((i + 1) % n) == 0:
                listaResult.append(auxlista)
                auxlista = []

        xStart = 0
        xStop = n - 1
        yStart = 0
        yStop = xStop
        i = 1
        print("Pusta lista: ", listaResult)

        def printData():
            print("\n")
            print("xStart:", xStart)
            print("xStop: ",xStop)
            print("yStart: ",yStart)
            print("yStop: ",yStop)
            print("i: ",i)
            print("\n")

        while i <= n**2:
            printData()
            for ix in range(xStart,xStop + 1):
                listaResult[yStart][ix] = i
                print("ix:", ix, " yStart: ", yStart, " i: ", i, " listaResult: ", listaResult)
                i += 1
            yStart += 1

            printData()
            for iy in range(yStart,yStop + 1):
                listaResult[iy][xStop] = i
                print("iy:", iy," xStop: ", xStop, " i: ", i," listaResult: ", listaResult)
                i += 1
            xStop -= 1

            printData()
            for ix in range(xStop,xStart-1,-1):
                listaResult[yStop][ix] = i
                print("ix:", ix, " yStop: ", yStop, " i: ", i, " listaResult: ", listaResult)
                i += 1
            yStop -= 1

            printData()
            for iy in range(yStop,yStart - 1,-1):
                listaResult[iy][xStart] = i
                print("iy:", iy, " xStart: ", xStart, " i: ", i, " listaResult: ", listaResult)
                i += 1
            xStart += 1

            # print("\nlistaResult: ",listaResult,"\n")
            if (n % 2 != 0) and (i == n**2):
                listaResult[n//2][n//2] = i

        return listaResult

    def generateMatrixFast(self, n: int) -> list[list[int]]:
        listaResult = [[0] * n for _ in range(n)]
        xStart = 0
        xStop = n - 1
        yStart = 0
        yStop = xStop
        i = 1

        while i <= n ** 2:
            for ix in range(xStart, xStop + 1):
                listaResult[yStart][ix] = i
                i += 1
            yStart += 1

            for iy in range(yStart, yStop + 1):
                listaResult[iy][xStop] = i
                i += 1
            xStop -= 1

            for ix in range(xStop, xStart - 1, -1):
                listaResult[yStop][ix] = i
                i += 1
            yStop -= 1

            for iy in range(yStop, yStart - 1, -1):
                listaResult[iy][xStart] = i
                i += 1
            xStart += 1

            if (n % 2 != 0) and (i == n ** 2):
                listaResult[n // 2][n // 2] = i

        return listaResult


Wynik = Solution()
print("Wynik: ",Wynik.generateMatrix(7))
print("Wynik: ",Wynik.generateMatrixFast(9))

# for ix in range(3,0,-1):
#     print(ix)