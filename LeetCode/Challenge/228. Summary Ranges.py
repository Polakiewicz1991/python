# ╔════════════════════════════════════╗
# ║ Sumowanie zasięgów wewnątrz listy: ║
# ║ Input:  [0,1,2,4,5,7]              ║
# ║ Output: ['0', '2->4', '6', '8->9'] ║
# ╚════════════════════════════════════╝
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if len(nums) < 1:
            return []

        i = 0
        lastNum = nums[i]
        rangesLists = []
        rangeList = [lastNum]

        for i in range(1,len(nums)):
            if nums[i] - lastNum > 1:
                rangesLists.append(rangeList)
                rangeList = []
                rangeList.append(nums[i])
            else:
                rangeList.append(nums[i])

            lastNum = nums[i]
        rangesLists.append(rangeList)
        # print(rangesLists)

        resultList = []

        for x in rangesLists:
            if len(x) == 1:
                resultList.append(str(x[0]))
            else:
                resultList.append(f"{x[0]}->{x[len(x) - 1]}")

        return resultList
Wynik = Solution()

nums = [0,1,2,4,5,7]
Wynik1 = Wynik.summaryRanges(nums= nums)
print("******\nWynik1", Wynik1, "\n******")

nums = [0,2,3,4,6,8,9]
Wynik1 = Wynik.summaryRanges(nums= nums)
print("******\nWynik1", Wynik1, "\n******")

nums = []
Wynik1 = Wynik.summaryRanges(nums= nums)
print("******\nWynik1", Wynik1, "\n******")
