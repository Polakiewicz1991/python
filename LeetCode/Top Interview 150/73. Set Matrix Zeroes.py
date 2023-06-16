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
        print(matrix, id(matrix))
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                matrix[i] = [0]*len(matrix[i])
                print(matrix[i])

        print(matrix,id(matrix))


Wynik = Solution()

matrix = [[1,1,1],[1,0,1],[1,1,1]]
Wynik1 = Wynik.setZeroes(matrix= matrix)
print("******\nWynik1", Wynik1, "\n******")