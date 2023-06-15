import math
from typing import List

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
class Solution:
    def maximumDetonationInt(self, bombs: List[List[int]]) -> int:
        graph = [[] for _ in bombs]
        for i, (xi, yi, ri) in enumerate(bombs):
            for j, (xj, yj, rj) in enumerate(bombs):
                if i < j:
                    dist2 = (xi - xj) ** 2 + (yi - yj) ** 2
                    if dist2 <= ri ** 2:
                        graph[i].append(j)
                    if dist2 <= rj ** 2:
                        graph[j].append(i)

        def fn(x):
            ans = 1
            seen = {x}
            stack = [x]
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if v not in seen:
                        ans += 1
                        seen.add(v)
                        stack.append(v)
            return ans

        return max(fn(x) for x in range(len(bombs)))
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        print("len(bombs)", len(bombs))
        #   Obliczanie pubkrów przecięcia - za dużo
        #   [X,Y,r]
        #   (x-x1)^2 +(y-y1)^2 = r^2
        #   x^2 + y^2 - 2x*x1 - 2y*y1 + x1^2 + y1^2 - r^2 = 0
        #   x^2 + y^2 = 2x*x1 + 2y*y1 - x1^2 - y1^2 + r^2
        #   [[2,1,3],[6,1,4]]
        #   2x*x1 + 2y*y1 - x1^2 - y1^2 + r^2
        #   2x*2 + 2y*1 - 2^2 - 1^2 + 3^2 = 2x*6 + 2y*1 - 6^2 - 1^2 + 4^2
        #   4x + 2y -4 - 1 +9 = 12x +2y - 36 - 1 + 16
        #   8x = -4 -21
        #   x = -3,125
        #   [[1,1,5],[10,10,5]]
        #   2x*1 + 2y*1 - 1^2 - 1^2 + 5^2 = 2x*10 + 2y*10 -10^2 -10^2 + 5^2
        #   2x +2y + 23 = 20x + 20y - 175
        #   Obliczanie odległości między środkami
        #   d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

        # <editor-fold> disc="Jest ok"
        dists = [1] * len(bombs)
        bombsExplode = {}
        for i1, bomb1 in enumerate(bombs):
            for i2, bomb2 in enumerate(bombs):
                if i1 != i2:
                    aux = ((bomb1[0] - bomb2[0])**2) + ((bomb1[1] - bomb2[1])**2)
                    # print(aux)
                    dist = math.sqrt(aux)
                    # print("i1", i1, "dist", dist)
                    # print( "dist", dist, "r", float(bomb1[2]) , float(bomb2[2]))
                    if (dist <= float(bomb1[2]) or dist <= float(bomb2[2])):
                        # print("bomb1", bomb1, "bomb2", bomb2, "dist", dist, "r", bomb1[2] , bomb2[2])
                        dists[i1] += 1
                        if tuple(bomb1) not in bombsExplode:
                            bombsExplode[tuple(bomb1)] = set()
                            # bombsExplode[i1].add(tuple(bomb1))
                            bombsExplode[tuple(bomb1)].add(tuple(bomb2))

                        else:
                            bombsExplode[tuple(bomb1)].add(tuple(bomb2))
        print(dists)
        # print(len(bombsExplode),bombsExplode)
        # bombsExplode.pop()
        i = 0
        sum = 1
        removed = set()
        while i < len(bombsExplode):
            keys = list(bombsExplode.keys())
            print((keys[i]))
            print(keys[i], ":", bombsExplode[keys[i]])
            explosions = set()
            explosions = explosions | bombsExplode[keys[i]]
            for bomb2 in bombsExplode[keys[i]]:
                if bomb2 not in removed:
                    explosions = explosions | bombsExplode[bomb2]
                    sum = max(sum,len(explosions))
                    if keys[i] != bomb2:
                        bombsExplode.pop(bomb2)
                        removed.add(bomb2)
                        print("removed", bomb2)
                    else:
                        sum += 1

            i +=1
        return sum  # max(dists)
        # sum = 1
        # for bomb in bombsExplode.keys():
        #     print(bomb, ":", bombsExplode[bomb])
        #     explosions = set()
        #     explosions = explosions | bombsExplode[bomb]
        #     for bomb2 in bombsExplode[bomb]:
        #         explosions = explosions | bombsExplode[bomb2]
        #         sum = max(sum,len(explosions))
        #         if bomb != bomb2:
        #             bombsExplode.pop(bomb2)
        # return sum#max(dists)
        # </editor-fold>

        # <editor-fold> disc="Jest nok"
        # dists = 1
        # for i in range(len(bombs)-1):
        #     bomb1= bombs[i]
        #     bomb2= bombs[i+1]
        #     aux = ((bomb1[0] - bomb2[0])**2) + ((bomb1[1] - bomb2[1])**2)
        #     # print(aux)
        #     dist = math.sqrt(aux)
        #     # print("i1", i1, "dist", dist)
        #     if (dist < bomb1[2] + bomb2[2]):
        #         print("bomb1", bomb1, "bomb2", bomb2, "dist", dist)
        #         dists += 1
        #
        # return (dists)
        # </editor-fold>

Wynik = Solution()
# bombs  = [[2,1,3],[6,1,4]]
# Wynik1 = Wynik.maximumDetonation(bombs= bombs)
# print("******\nWynik1", Wynik1, "\n******")
#
# bombs = [[1,1,5],[10,10,5]]
# Wynik1 = Wynik.maximumDetonation(bombs= bombs)
# print("******\nWynik1", Wynik1, "\n******")
#
# bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
# Wynik1 = Wynik.maximumDetonation(bombs= bombs)
# print("******\nWynik1", Wynik1, "\n******")
#
# bombs = [[54,95,4],[99,46,3],[29,21,3],[96,72,8],[49,43,3],[11,20,3],[2,57,1],[69,51,7],[97,1,10],[85,45,2],[38,47,1],[83,75,3],[65,59,3],[33,4,1],[32,10,2],[20,97,8],[35,37,3]]
# Wynik1 = Wynik.maximumDetonation(bombs= bombs)
# print("******\nWynik1", Wynik1, "\n******")
#
# bombs = [[56,80,2],[55,9,10],[32,75,2],[87,89,1],[61,94,3],[43,82,9],[17,100,6],[50,6,7],[9,66,7],[98,3,6],[67,50,2],[79,39,5],[92,60,10],[49,9,9],[42,32,10]]
# Wynik1 = Wynik.maximumDetonation(bombs= bombs)
# print("******\nWynik1", Wynik1, "\n******")
#
# bombs = [[94,70,8],[4,65,1],[95,97,6],[16,32,9],[31,28,5],[18,95,1],[29,42,10],[99,41,1],[95,34,4],[1,89,3],[82,12,10],[5,87,10],[74,88,4],[28,49,8],[69,64,2]]
# Wynik1 = Wynik.maximumDetonation(bombs= bombs)
# print("******\nWynik1", Wynik1, "\n******")

bombs = [[656,619,56],[189,402,178],[513,373,276],[900,510,14],[188,173,129],[512,178,251],[145,685,47],[504,355,500],[554,131,214],[596,1,98],[358,230,197],[88,758,155],[72,340,419],[818,708,222]]
Wynik1 = Wynik.maximumDetonation(bombs= bombs)
print("******\nWynik1", Wynik1, "\n******")

bombs = [[4,4,3],[4,4,3]]
Wynik1 = Wynik.maximumDetonation(bombs= bombs)
print("******\nWynik1", Wynik1, "\n******")

bombs = [[855,82,158],[17,719,430],[90,756,164],[376,17,340],[691,636,152],[565,776,5],[464,154,271],[53,361,162],[278,609,82],[202,927,219],[542,865,377],[330,402,270],[720,199,10],[986,697,443],[471,296,69],[393,81,404],[127,405,177]]
Wynik1 = Wynik.maximumDetonation(bombs= bombs)
print("******\nWynik1", Wynik1, "\n******")

# def draw_circle(x, y, r):
#     circle = Circle((x, y), r, edgecolor='r', facecolor='none')
#     plt.gca().add_patch(circle)
#     plt.text(x, y, f"({x}, {y})", ha='center', va='bottom')
#     center_circle = Circle((x, y), 0.1, edgecolor='r', facecolor='r')
#     plt.gca().add_patch(center_circle)
#
# def draw_circles(*circles):
#     for circle in circles:
#         x, y, r = circle
#         circle = Circle((x, y), r, edgecolor='b', facecolor='none')
#         plt.gca().add_patch(circle)
#         plt.text(x, y, f"({x}, {y})", ha='center', va='bottom')
#         center_circle = Circle((x, y), 10, edgecolor='r', facecolor='r')
#         plt.gca().add_patch(center_circle)
# # def draw_bombs(*circles):
# #     for circle in circles:
# #         x, y, r = circle
# #         circle = Circle((x, y), r, edgecolor='y', facecolor='none')
# #         plt.gca().add_patch(circle)
# #
# #
# # # # Dane okręgów
# # # # circle1 = [65, 59, 3]
# # # # circle2 = [69, 51, 7]
# # #
# # # # circle1 = [29, 42, 10]
# # # # circle2 = [16, 32, 9]
# # # # circle3 = [31, 28, 5]
# # # # circle4 = [28, 49, 8]
# # #
# # # circle1 = [2,1,3]
# # # circle2 = [6,1,4]
# #
# # circles = [[504, 355, 500], [656, 619, 56], [189, 402, 178], [513, 373, 276], [900, 510, 14], [188, 173, 129], [512, 178, 251], [145, 685, 47], [554, 131, 214], [596, 1, 98], [358, 230, 197], [72, 340, 419], [818, 708, 222]]
# # # bombs = [[656,619,56],[189,402,178],[513,373,276],[900,510,14],[188,173,129],[512,178,251],[145,685,47],[504,355,500],[554,131,214],[596,1,98],[358,230,197],[88,758,155],[72,340,419],[818,708,222]]
# # exception = [88, 758, 155]
# #
#
# circles = [[855,82,158],[17,719,430],[90,756,164],[376,17,340],[691,636,152],[565,776,5],[464,154,271],[53,361,162],[278,609,82],[202,927,219],[542,865,377],[330,402,270],[720,199,10],[986,697,443],[471,296,69],[393,81,404],[127,405,177]]
#
# # # circleSet = set()
# # # bombsSet = set()
# # # for circle in circles:
# # #     circleSet.add(tuple(circle))
# # # for bomb in bombs:
# # #     bombsSet.add(tuple(bomb))
# # # print("xD",bombsSet - circleSet)
# #
# # Inicjalizacja wykresu
# fig, ax = plt.subplots()
# #
# # # Rysowanie okręgów
# draw_circles(*circles)
# # draw_circle(*exception)
# # # draw_bombs(*circles)
# #
# # # draw_circle(*circle1)
# # # draw_circle(*circle2)
# # # draw_circle(*circle3)
# # # draw_circle(*circle4)
# #
# # Ustawienie granic osi x i y
# ax.set_xlim(0, 100)
# ax.set_ylim(0, 100)
#
# # Wyświetlenie wykresu
# plt.axis('scaled')
# plt.show()