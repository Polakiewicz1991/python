from typing import List
import math
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        first = coordinates[0]
        last = coordinates[len(coordinates) - 1]
        if last[0] - first[0] != 0:
            a = (last[1] - first[1])/(last[0] - first[0])
            b = first[1] - a * first[0]
        else:
            a = math.inf
            b = 0

        print("a", a, "b", b)

        for x in coordinates:
            print(f"{x[0]}, {x[1]} =", a * x[0] + b)
            if a == math.inf:
                if x[0] == first[0]:
                    continue
                else:
                    return False
            else:
                if x[1] == a * x[0] + b:
                    continue
                else:
                    return False
        return True

Wynik = Solution()
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Wynik1 = Wynik.checkStraightLine(coordinates= coordinates)
print("******\nWynik1", Wynik1, "\n******")

coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Wynik1 = Wynik.checkStraightLine(coordinates= coordinates)
print("******\nWynik1", Wynik1, "\n******")

coordinates = [[0,0],[0,1],[0,-1]]
Wynik1 = Wynik.checkStraightLine(coordinates= coordinates)
print("******\nWynik1", Wynik1, "\n******")

coordinates = [[3,0],[3,2],[3,-2]]
Wynik1 = Wynik.checkStraightLine(coordinates= coordinates)
print("******\nWynik1", Wynik1, "\n******")

coordinates = [[2,1],[4,2],[6,3]]
Wynik1 = Wynik.checkStraightLine(coordinates= coordinates)
print("******\nWynik1", Wynik1, "\n******")