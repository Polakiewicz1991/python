from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        heightLen = len(height)
        res = 0
        i = 0
        wallLH = []
        wallRH = []
        ratioLH = 0
        ratioRH = 0
        iLH = 0
        iRH = heightLen - 1
        while i < heightLen:

            if ratioLH < height[i] / (i + 1):
                ratioLH = height[i] / (i + 1)
                iLH = i
            wallLH.append([height[i],i,ratioLH])

            if ratioRH < height[heightLen - 1 - i] / (i + 1):
                ratioRH = (height[heightLen - 1 - i])/ (i + 1)
                iRH = heightLen - 1 - i
                print("ratioRH",ratioRH)
            wallRH.append([height[heightLen - 1 - i], heightLen - 1 - i,ratioRH])

            # res = min(height[iLH], height[iRH]) * (wallLH[iRH][1] - wallLH[iLH][1])

            i += 1

        # wallLH += reversed(wallRH)
        print(iLH,ratioLH)
        print(iRH, ratioRH)
        print(wallLH)
        print(wallRH)
        return min(height[iLH],height[iRH]) * (wallLH[iRH][1] - wallLH[iLH][1])

    def maxArea(self, height: List[int]) -> int:
        # two pointer question
        max_area = 0
        current = 0
        l = 0  # initialize left pointer
        r = len(height) - 1  # initialize right pointer
        while l < r:
            current = (r - l) * min(height[l], height[r])
            next1 = (r - 1 - l) * min(height[l], height[r - 1])  # right pointer minus 1
            next2 = (r - l - 1) * min(height[l + 1], height[r])  # left pointer plus 1
            next3 = (r - 2 - l) * min(height[l + 1], height[r - 1])  # left pointer plus 1, right minus 1
            max_area = max(current, next1, next2, next3, max_area)
            print(current, next1, next2, next3, max_area)
            if height[l] <= height[r]:
                print("l+")
                l += 1
            elif height[l] > height[r]:
                print("r-")
                r -= 1
            print("height",height[l:r])
        return max_area

Wynik = Solution()

height = [1,8,6,2,5,4,8,3,7]
# Output: 49
Wynik1 = Wynik.maxArea(height= height)
print("******\nWynik1", Wynik1, "\n******")

height = [1,1]
Wynik1 = Wynik.maxArea(height= height)
print("******\nWynik1", Wynik1, "\n******")

height = [1,2,4,3]
Wynik1 = Wynik.maxArea(height= height)
print("******\nWynik1", Wynik1, "\n******")