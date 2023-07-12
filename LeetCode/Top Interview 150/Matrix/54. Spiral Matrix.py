import time
class Solution:
    def spiralOrder2(self, matrix: list[list[int]]) -> list[int]:
        xLen = len(matrix[0])
        yLen = len(matrix)
        resultList = []
        print(xLen)
        print(yLen)
        y = 0
        i = 0
        k = 0
        while len(resultList) < yLen * xLen:
            j = xLen - i - 1
            k = yLen - i - 1
            print("i: ", i)
            print("j:", j)
            print("k:", k)
            print("y: ", y)

            if i % 2 == 0:
                if y == i and not(y == k):
                    print("matrix[y][i:j]",matrix[y][i:j+1])
                    resultList += (matrix[y][i:j+1])
                elif y == k:
                    print("matrix[y][::-1]",matrix[y][::-1])
                    resultList += (matrix[y][::-1])
                    i += 1
                else:
                    print("matrix[y][j]",matrix[y][j])
                    resultList += [matrix[y][j]]

            else:
                if y == i:
                    print("y == i:",matrix[y][(i-1):j+1])
                    resultList += (matrix[y][(i-1):j+1])
                    i += 1
                # elif y == k:
                #     print("y == j - 1:",matrix[y][::-1])
                #     resultList += (matrix[y][::-1])
                else:
                    print("matrix[y][(i - 1):j]",matrix[y][(i - 1)])
                    resultList += [matrix[y][(i - 1)]]

            if i % 2 == 0:
                y += 1
            else:
                y -= 1

            print("resultList: ", resultList)
            print("resultList lenght: ", len(resultList))
            print("\n")
        return resultList

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        xLen = len(matrix[0])
        yLen = len(matrix)
        resultList = []

        y = 0
        yStart = y
        yStop = yLen - y - 1

        xStart = 0
        xStop = xLen

        i = 0

        while len(resultList) < yLen * xLen:
            if i % 2 == 0:
                if y == yStart:
                    resultList += (matrix[y][xStart:xStop])
                elif y == yLen - 1:
                    resultList += (matrix[y][::-1])
                    i += 1
                    yStart += 1
                    xStop -= 1
                elif y == yStop:
                    resultList += (matrix[y][xStop-1:xStart-1:-1])
                    i += 1
                    yStart += 1
                    xStop -= 1
                else:
                    resultList += [matrix[y][xStop - 1]]
            else:
                if y == yStart:
                    resultList += (matrix[y][xStart:xStop])
                    i += 1
                    yStop -= 1
                    xStart += 1

                elif y == yStop:
                    resultList += (matrix[y][xStop:xStart:-1])
                    i += 1
                else:
                    resultList += [matrix[y][xStart]]

            if i % 2 == 0:
                y += 1
            else:
                y -= 1

        return resultList

    def spiralOrderInternet(self, matrix: list[list[int]]) -> list[int]:
        height = len(matrix)
        width = len(matrix[0])

        top = 0
        bottom = height - 1
        left = 0
        right = width - 1

        ans = []
        while top < bottom and left < right:
            for col in range(left, right):
                ans.append(matrix[top][col])

            for row in range(top, bottom):
                ans.append(matrix[row][right])

            for col in range(right, left, -1):
                ans.append(matrix[bottom][col])

            for row in range(bottom, top, -1):
                ans.append(matrix[row][left])

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        # If a matrix remain inside it is either a 1xn or a mx1
        # a linear scan will return the same order as spiral for these
        if len(ans) < height * width:
            for row in range(top, bottom + 1):
                for col in range(left, right + 1):
                    ans.append(matrix[row][col])

        return ans
timeStart = time.time()
Wynik = Solution()

lista1 = []
auxlista = []
divisor = 10
for i in range(divisor**2):
    auxlista += [i]
    print("auxlista: ",auxlista)
    print("i+1 % {0}: ".format(divisor),((i + 1) % divisor))
    if ((i + 1) % divisor) == 0:
        lista1.append(auxlista)
        auxlista = []

print("lista1: ",lista1)
for string in lista1:
    print(string)
print("\n\n\n\n")
# lista2 = Wynik.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])

print("timeStart: ",timeStart)
lista3 = Wynik.spiralOrder(lista1)
timeStop = time.time()
print("timeStop: ",timeStop)
timeLista3 = timeStart - timeStop
timeStart = time.time()
lista4 = Wynik.spiralOrderInternet(lista1)
timeStop = time.time()
timeLista4 = timeStart - timeStop
# print("1: ",lista1)
# print("2: ",lista2)
print("\n\n\n\n")
print("3: ",lista3)
print("time lista 3: ",timeLista3)
print("4: ",lista4)
print("time lista 4: ",timeLista4)


lista = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(lista[1][0::]) #[5, 6, 7, 8]
# print(lista[1][0:3:]) #[5, 6, 7]
# print(lista[1][0:4:]) #[5, 6, 7, 8]
# print(lista[1][0::-1]) #[5]
# print("\n\n\n\n")
# print(lista[1][3::-1]) #
# print(lista[1][0::-1]) #[5]
# print(lista[1][1:0:-1]) #[6]
print(lista[1][3:0:-1]) #[8, 7, 6]
# print(lista[1][3:0:-1]) #[8, 7, 6]
# print(lista[1][2::-1]) #[7, 6, 5]
# print(lista[1][2:0:-1]) #[7, 6]
# print(lista[1][2:1:-1]) #[7]
# print(lista[1][2:2:-1]) #[]
