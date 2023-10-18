# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
# return the maximum number of points that lie on the same straight line.

from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2: return len(points)
        finLinDict = {}

        i = 0
        res = 0


        while i < len(points):
            j = i
            resJ = 0

            while j < len(points):
                if points[i][0] - points[j][0] != 0:
                    #[x,y] => [0,1]
                    #a = (y2 - y1)/(x2 - x1)
                    #b = y1 - a * x1

                    ai = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    bi = points[i][1] - (ai * points[i][0])
                    bj = points[j][1] - (ai * points[j][0])

                    nameDictAi = str(ai)[:4] + ":" + str(bi)[:4]
                    nameDictAj = str(ai)[:4] + ":" + str(bj)[:4]
                    # nameDictAi = nameDictAi[:20]
                    # nameDictAj = nameDictAj[:20]


                    if nameDictAi in finLinDict:
                        if points[i] not in finLinDict[nameDictAi]:
                            finLinDict[nameDictAi].append(points[i])
                    else:
                        finLinDict[nameDictAi] = [points[i]]

                    if nameDictAj in finLinDict:
                        if points[j] not in finLinDict[nameDictAj]:
                            finLinDict[nameDictAj].append(points[j])
                    else:
                        finLinDict[nameDictAj] = [points[j]]
                    j += 1
                else:
                    bi = points[i][1]
                    bj = points[j][1]
                    nameDictAi = str("x") + ":" + str(points[i][0])
                    nameDictAj = str("x") + ":" + str(points[j][0])

                    if nameDictAi in finLinDict:
                        if points[i] not in finLinDict[nameDictAi]:
                            finLinDict[nameDictAi].append(points[i])
                    else:
                        finLinDict[nameDictAi] = [points[i]]

                    if nameDictAj in finLinDict:
                        if points[j] not in finLinDict[nameDictAj]:
                            finLinDict[nameDictAj].append(points[j])
                    else:
                        finLinDict[nameDictAj] = [points[j]]

                    j += 1
            i += 1
        # print(finLinDict)

        res = 0
        for x in finLinDict.values():
            res = max(res,len(x))
        listalista = list(finLinDict.keys())
        print("\n\n\n",listalista.sort())
        return res

    def maxPointsChatGPT(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)

        max_points = 2  # Minimum 2 punkty, gdyż prosta jest opisana przez co najmniej 2 punkty

        for i, p1 in enumerate(points):
            slopes = {}  # Słownik przechowujący nachylenia dla punktu p1
            same_point = 0  # Liczba punktów identycznych z p1

            for j, p2 in enumerate(points):
                if i != j:
                    if p1 == p2:
                        same_point += 1
                    elif p2[0] == p1[0]:
                        # Obsługa nachylenia równe 0 (pozioma linia)
                        slope = "inf"
                        if slope not in slopes:
                            slopes[slope] = 1
                        else:
                            slopes[slope] += 1
                    else:
                        # Obliczenie nachylenia i zaokrąglenie do 5 miejsc po przecinku
                        slope = round((p2[1] - p1[1]) / (p2[0] - p1[0]), 10)

                        if slope not in slopes:
                            slopes[slope] = 1
                        else:
                            slopes[slope] += 1

            if slopes:
                max_points = max(max_points, max(slopes.values()) + same_point + 1)
            else:
                max_points = max(max_points, same_point + 1)

        return max_points



Wynik = Solution()

points = [[1,1],[2,2],[3,3]]
print("\n\npoints=", points)
Wynik1 = Wynik.maxPoints(points=points)
print("******\nWynik1", Wynik1, "\n******")

points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print("\n\npoints=", points)
Wynik1 = Wynik.maxPoints(points=points)
print("******\nWynik1", Wynik1, "\n******")

points = [[0,0]]
print("\n\npoints=", points)
Wynik1 = Wynik.maxPoints(points=points)
print("******\nWynik1", Wynik1, "\n******")

points = [[0,0],[1,-1],[1,1]]
print("\n\npoints=", points)
Wynik1 = Wynik.maxPoints(points=points)
print("******\nWynik1", Wynik1, "\n******")


points = [[4,5],[4,-1],[4,0]]
print("\n\npoints=", points)
Wynik1 = Wynik.maxPoints(points=points)
print("******\nWynik1", Wynik1, "\n******")



points = [[-6,-1],[3,1],[12,3]]
print("\n\npoints=", points)
Wynik1 = Wynik.maxPoints(points=points)
print("******\nWynik1", Wynik1, "\n******")

points = [[7,3],[19,19],[-16,3],[13,17],[-18,1],[-18,-17],[13,-3],[3,7],[-11,12],[7,19],[19,-12],[20,-18],[-16,-15],[-10,-15],[-16,-18],[-14,-1],[18,10],[-13,8],[7,-5],[-4,-9],[-11,2],[-9,-9],[-5,-16],[10,14],[-3,4],[1,-20],[2,16],[0,14],[-14,5],[15,-11],[3,11],[11,-10],[-1,-7],[16,7],[1,-11],[-8,-3],[1,-6],[19,7],[3,6],[-1,-2],[7,-3],[-6,-8],[7,1],[-15,12],[-17,9],[19,-9],[1,0],[9,-10],[6,20],[-12,-4],[-16,-17],[14,3],[0,-1],[-18,9],[-15,15],[-3,-15],[-5,20],[15,-14],[9,-17],[10,-14],[-7,-11],[14,9],[1,-1],[15,12],[-5,-1],[-17,-5],[15,-2],[-12,11],[19,-18],[8,7],[-5,-3],[-17,-1],[-18,13],[15,-3],[4,18],[-14,-15],[15,8],[-18,-12],[-15,19],[-9,16],[-9,14],[-12,-14],[-2,-20],[-3,-13],[10,-7],[-2,-10],[9,10],[-1,7],[-17,-6],[-15,20],[5,-17],[6,-6],[-11,-8]]
print("\n\npoints=", points)
Wynik1 = Wynik.maxPoints(points=points)
print("******\nWynik1", Wynik1, "\n******")

points = [[-184,-551],[-105,-467],[-90,-394],[-60,-248],[115,359],[138,429],[60,336],[150,774],[207,639],[-150,-686],[-135,-613],[92,289],[23,79],[135,701],[0,9],[-230,-691],[-115,-341],[-161,-481],[230,709],[-30,-102]]
print("\n\npoints=", points)
Wynik1 = Wynik.maxPointsChatGPT(points=points)
print("******\nWynik1", Wynik1, "\n******")