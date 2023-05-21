from typing import List
class PointMatrix:
    def __init__(self,*points,lenght):
        self.points = points
        self.island1: set = {None}
        self.island2: set = {None}
        self.lenght = lenght

    def __str__(self):
        strResult = ""
        for point in self.points:
            # print("points",point)
            strResult += f"{point.name} is island = {point.island}, connected:{point.connected}, connections: {point.connections}.\n"
        strResult += f"Numbers of point in matrix {len(self.points)}"
        return strResult

    def addPoint(self,*points):
        self.points += points

    def checkPointConnectons(self):
        for point in self.points:
            if point.island == True and point.connected == False:
                #znajdż nie wyspę płączoną z inn
                pass

    def createIslands(self):

        mapping_points = {point.name: point for point in self.points}

        for x in range(self.lenght):
            for y in range(self.lenght):
                print(f"P{y}{x}: ", mapping_points[f"P{y}{x}"])



        for point in self.points:
            if point.island == True and point.connected == False:
                print("point.y", point.y)
                print("point.x", point.x)
                print("[point.y,point.x]", (point.y, point.x))
                xs = [point.y, point.x]
                self.island1.add(tuple(xs))
                for connections in point.connections["1"]:
                    self.island1.add(tuple(connections))


class PointConnection:
    def __init__(self,x:  int, y: int):
        self.name = f"P{y}{x}"
        self.x = x
        self.y = y
        self.island = False
        self.connected = False
        self.connections = {"0": [],
                            "1": []}

    def __str__(self):
        return f"{self.name} is island = {self.island},connected {self.connected}, connections: {self.connections}."

    @classmethod
    def createPoint(self, x, y) -> "PointConnection":
        return PointConnection(x, y)

    def checkConnection(self, grid: List[List[int]]):
        xLen = len(grid[0])
        if grid[self.y][self.x] == 1:
            self.island = True
        for iX in [-1, 1]:
            # print("y:", self.y, " x + iX:", self.x + iX)
            if self.x + iX >= 0 and self.x + iX <= xLen - 1:
                if grid[self.y][self.x + iX] == 1:
                    self.connected = True
                    self.connections["1"].append([self.y,self.x + iX])
                elif grid[self.y][self.x + iX] == 0:
                    self.connections["0"].append([self.y, self.x + iX])
                    # self.connections["0"] = self.connections["0"] + [self.y,self.x + iX]

        for iY in [-1, 1]:
            # print("y:", self.y, " x + iX:", self.x + iX)
            if self.y + iY >= 0 and self.y + iY <= xLen - 1:
                if grid[self.y + iY][self.x] == 1:
                    self.connected = True
                    self.connections["1"].append([self.y + iY,self.x])
                    # self.connections["1"] = self.connections["1"] + [self.y + iY,self.x]
                elif grid[self.y + iY][self.x] == 0:
                    self.connections["0"].append([self.y + iY, self.x])
                    # self.connections["0"] = self.connections["0"] + [self.y + iY,self.x]


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        xLen = len(grid)
        Matrix = PointMatrix(lenght= xLen)
        for y in range(xLen):
            # print("y: ", y)
            for x in range(xLen):
                # print("x: ", x)
                Matrix.addPoint(PointConnection.createPoint(y,x))

        for point in Matrix.points:
            point.checkConnection(grid)

        Matrix.createIslands()
        print("island1",Matrix.island1)
        print("Matrix:\n", Matrix)
        # print(Matrix.points[0])

Wynik = Solution()
grid = [[0,1],
        [1,0]]
Wynik1 = Wynik.shortestBridge(grid)
print("Wynik1: ", Wynik1, "\n")
#
# grid = [[0,1,0],
#         [0,0,0],
#         [0,0,1]]
# Wynik2 = Wynik.shortestBridge(grid)
# print("Wynik2: ", Wynik2, "\n")
#
# grid = [[1,1,1,1,1],
#         [1,0,0,0,1],
#         [1,0,1,0,1],
#         [1,0,0,0,1],
#         [1,1,1,1,1]]
# Wynik3 = Wynik.shortestBridge(grid)
# print("Wynik3: ", Wynik3, "\n")