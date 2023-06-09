# ║ zerowanie macierzy gdy "0" w liscie║
# ║ Transponowanie tabeli              ║
# ║                                    ║
# ╚════════════════════════════════════╝
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # print(matrix, id(matrix))
        zerolist = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zerolist.append(j)
            if 0 in matrix[i]:
                matrix[i] = [0]*len(matrix[i])
                # print(matrix[i])
        # print(zerolist)

        for x in zerolist:
            for i in range(len(matrix)):
                matrix[i][x] = 0
                # print(x,i)

        # print(matrix, id(matrix))

Wynik = Solution()

matrix = [[1,1,1],[1,0,1],[1,1,1]]
Wynik1 = Wynik.setZeroes(matrix= matrix)
print("******\nWynik1", Wynik1, "\n******")