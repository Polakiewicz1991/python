from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #[Y,X]
        gridLen = len(grid) - 1
        counter = 1
        position = (0,0)
        print("Y:", position[0], "X:", position[1])
        stop = (gridLen,gridLen)
        if grid[0][0] !=0 or grid[gridLen][gridLen] != 0:
            return -1
        def findNearZeros(position: List[int], counter):
            print(f"{counter}: ","position", position)
            zeroNear = set()
            zeroCheck = [0, 0]
            grid[position[0]][position[1]] = 1
            for y in range(-1,2):
                for x in range (-1,2):
                    # print(x,y)
                    if not (x == 0 and y == 0):
                        if (position[1] + x >= 0 and position[1] + x <= gridLen):
                            if position[0] + y >= 0 and position[0] + y <= gridLen:
                                zeroCheck[0] = position[0] + y
                                zeroCheck[1] = position[1] + x
                                if grid[zeroCheck[0]][zeroCheck[1]] == 0:
                                    print(f"{counter}: ", (zeroCheck[0],zeroCheck[1]))
                                    zeroNear.add((zeroCheck[0],zeroCheck[1]))
            print("zeroNear", zeroNear)

            if stop in zeroNear:
                return counter
            else:
                for zero in zeroNear:
                    return findNearZeros(position= zero, counter= counter + 1)

        return findNearZeros(position= position, counter= counter)

    def shortestPathBinaryMatrixInternet(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        queue = [(0, 0, 1)]
        grid[0][0] = 1

        for i, j, d in queue:
            if i == n - 1 and j == n - 1:
                return d

            directions = [
                (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                (i, j - 1), (i, j + 1),
                (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
            ]

            for x, y in directions:
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1
                    queue.append((x, y, d + 1))
            print("grid", grid)
            print("queue", queue)
        return -1


Wynik = Solution()
grid = [[0,0,0],[1,1,0],[1,1,0]]
Wynik1 = Wynik.shortestPathBinaryMatrix(grid= grid)
print("Wynik1", Wynik1)

grid = [[1,0,0],[1,1,0],[1,1,0]]
Wynik1 = Wynik.shortestPathBinaryMatrix(grid= grid)
print("Wynik1", Wynik1)

grid = [[0,1],[1,0]]
Wynik1 = Wynik.shortestPathBinaryMatrix(grid= grid)
print("Wynik1", Wynik1)