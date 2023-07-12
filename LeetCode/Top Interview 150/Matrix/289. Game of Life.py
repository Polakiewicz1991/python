# ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ According to Wikipedia's article: "The Game of Life, also known simply as Life,                         ║
# ║ is a cellular automaton devised by the British mathematician John Horton Conway in 1970."               ║
# ║                                                                                                         ║
# ║ The board is made up of an m x n grid of cells, where each cell has an initial state:                   ║
# ║ live (represented by a 1) or dead (represented by a 0).                                                 ║
# ║ Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)                           ║
# ║ using the following four rules (taken from the above Wikipedia article):                                ║
# ║                                                                                                         ║
# ║    Any live cell with fewer than two live neighbors dies as if caused by under-population.              ║
# ║    Any live cell with two or three live neighbors lives on to the next generation.                      ║
# ║    Any live cell with more than three live neighbors dies, as if by over-population.                    ║
# ║    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.          ║
# ║                                                                                                         ║
# ║ The next state is created by applying the above rules simultaneously to every cell in the current state,║
# ║ where births and deaths occur simultaneously. Given the current state of the m x n grid board,          ║
# ║ return the next state.                                                                                  ║
# ║                                                                                                         ║
# ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════╝
from typing import List
import copy

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rangeY = len(board)
        rangeX = len(board[0])
        boardAux = copy.deepcopy(board)
        def checkNeighbours(y,x):
            checklist = []
            for yi in range(-1,2):
                for xi in range(-1, 2):
                    if y + yi >= 0 and y + yi < rangeY:
                        if x + xi >= 0 and x + xi < rangeX:
                            if not (xi == 0 and yi == 0):
                                # print("yi:", yi, "xi:", xi, "y:", y + yi, "x:", x + xi)
                                checklist.append(boardAux[y + yi][x + xi])
                                # print(boardAux[y + yi][x + xi])

            if checklist.count(1) < 2 and board[y][x] == 1:
                board[y][x] = 0
            elif checklist.count(1) > 3 and board[y][x] == 1:
                board[y][x] = 0
            elif checklist.count(1) >= 2 and board[y][x] == 1:
                pass
            elif checklist.count(1) == 3 and board[y][x] == 0:
                board[y][x] = 1

        #     print(checklist)
        #
        # print(board, id(board),boardAux, id(boardAux))

        for y in range(rangeY):
            for x in range(rangeX):
                checkNeighbours(y, x)
        # print(board)
        # print(boardAux)
        # print("0,0")
        # checkNeighbours(0,0)
        # print("1,1")
        # checkNeighbours(1, 1)
        # print("2,2")
        # checkNeighbours(2, 2)


Wynik = Solution()

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Wynik1 = Wynik.gameOfLife(board= board)
print("******\nWynik1", Wynik1, "\n******")

board = [[1,1],[1,0]]
Wynik1 = Wynik.gameOfLife(board= board)
print("******\nWynik1", Wynik1, "\n******")
# testy z id
matrix = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
#różne id, te same elementy
matrix_2  = matrix.copy()
print(matrix, id(matrix),matrix_2, id(matrix_2))
print(matrix[1][1], id(matrix[1][1]),matrix_2[1][1], id(matrix_2[1][1]))
print(matrix[2], id(matrix[2]),matrix_2[2], id(matrix_2[2]))
#różne id, te same elementy
matrix_2  = matrix[:]
print(matrix, id(matrix),matrix_2, id(matrix_2))
print(matrix[1][1], id(matrix[1][1]),matrix_2[1][1], id(matrix_2[1][1]))
print(matrix[2], id(matrix[2]),matrix_2[2], id(matrix_2[2]))
#różne id, te same elementy
matrix_2 = [row[:] for row in matrix]
print(matrix, id(matrix),matrix_2, id(matrix_2))
print(matrix[1][1], id(matrix[1][1]),matrix_2[1][1], id(matrix_2[1][1]))
print(matrix[2], id(matrix[2]),matrix_2[2], id(matrix_2[2]))

# Skopiowanie listy w liście
matrix_2 = [[item for item in sublist] for sublist in matrix]
print(matrix, id(matrix),matrix_2, id(matrix_2))
print(matrix[1][1], id(matrix[1][1]),matrix_2[1][1], id(matrix_2[1][1]))
print(matrix[2], id(matrix[2]),matrix_2[2], id(matrix_2[2]))