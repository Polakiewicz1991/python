# ╔════════════════════════════════════╗
# ║ Sprawdzanie poprawności sudoku:    ║
# ║ Transponowanie tabeli              ║
# ║                                    ║
# ╚════════════════════════════════════╝
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(matrix, id(matrix))
        for i in range((len(matrix))//2):
            print(i,len(matrix)-1-i)
            matrix[i],matrix[len(matrix)-1-i] = matrix[len(matrix)-1-i], matrix[i]

        print(matrix, id(matrix))
        # matrix = list(zip(*matrix))
        for x in range(0,len(matrix)):
            for y in range(x,len(matrix)):
                print(x, y)
                print(y, x, "\n")

                tempVal = matrix[y][x]
                matrix[y][x] = matrix[x][y]
                matrix[x][y] = tempVal
        print(matrix, id(matrix))

Wynik = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
Wynik1 = Wynik.rotate(matrix= matrix)
print("******\nWynik1", Wynik1, "\n******")


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Wynik1 = Wynik.rotate(matrix= matrix)
print("******\nWynik1", Wynik1, "\n******")
# [x00,x01,x02]
# [x10,x11,x12]
# [x20,x21,x22]

# [x00,x10,x20]
# [x01,x11,x21]
# [x02,x12,x22]

# [[7,4,1],[8,5,2],[9,6,3]]
# [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

