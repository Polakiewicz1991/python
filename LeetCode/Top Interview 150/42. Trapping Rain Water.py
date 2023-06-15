from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxHeight = max(height)
        # print("maxHeight", maxHeight)
        ranges = {}

        def addWater(water: List[int]) -> int:
            res = 0
            if len(water) > 1:
                water.sort()
                for i in range(len(water) - 1):
                    if (water[i + 1] - water[i]) > 1:
                        res += (water[i + 1] - water[i]) - 1
                return  res
            else:
                return 0
        topRange = []

        for i in range(maxHeight,-1,-1):
            # print("i:", i)
            rangesI = []
            for j in enumerate(height):
                if i == j[1]:
                     rangesI.append(j[0])
                ranges[i] = rangesI

            topRange = topRange + rangesI
            res += addWater(topRange)
            # print("topRange ", topRange, " res: ", res)
        # print(ranges)
        return res

    def trap2(self, height: List[int]) -> int:
        wallPrev = (0, height[0])
    #     #   [0,1,0,2,1,0,1,3,2,1,2,1]
    #     #   [_,_,1,_,1,2,1,_,_,1,_,_]
    #         [0,1,1,2,2,2,2,3,3,3,3,3]
    #         [3,3,3,3,3,3,3,3,2,2,2,1]

    #         [0,1,1,2,2,2,2,3,2,2,2,1]
    #         [0,0,1,0,1,2,1,0,0,1,0,1]

    #     #   [5,1,0,2,1,0,1,3,2,1,2,1]
    #     #   [_,2,3,1,2,3,2,_,_,1,_,_]
    #     #   [4,2,0,3,2,5]
    #     #   [_,2,4,1,3,_]
    #     #   [4,2,0,6,2,5]
    #     #   [_,2,4,_,3,_]
    #
        res = 0
        lenHeight = len(height)
        lMaxVal = height[0]
        rMaxVal = height[lenHeight - 1]
        lMax = [lMaxVal]
        rMax = [rMaxVal]
        for i in range(1, lenHeight):
            # print("i", i)
            j = lenHeight - 1 - i
            lMaxVal = max(lMaxVal,height[i])
            rMaxVal = max(rMaxVal, height[j])

            lMax.append(lMaxVal)
            rMax.insert(0,rMaxVal)

        for i in range(lenHeight):
            res += min(lMax[i],rMax[i]) - height[i]
        return res




Wynik = Solution()


height = [0,1,0,2,1,0,1,3,2,1,2,1]
Wynik1 = Wynik.trap(height= height)
print("Wynik1", Wynik1)

height = [4,2,0,3,2,5]
Wynik1 = Wynik.trap(height= height)
print("Wynik1", Wynik1)

height = [5,1,0,2,1,0,1,3,2,1,2,1]
Wynik1 = Wynik.trap(height= height)
print("Wynik1", Wynik1)

height = [4,2,0,6,2,5]
Wynik1 = Wynik.trap(height= height)
print("Wynik1", Wynik1)

#   [0,1,0,2,1,0,1,3,2,1,2,1]
#   [_,_,1,_,1,2,1,_,_,1,_,_]
#   [5,1,0,2,1,0,1,3,2,1,2,1]
#   [_,2,3,1,2,3,2,_,_,1,_,_]