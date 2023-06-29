# ╔═════════════════════════════════════════════════════════════════════╗
# ║ Given an unsorted array of integers nums, return the length         ║
# ║ of the longest consecutive elements sequence.                       ║
# ║ You must write an algorithm that runs in O(n) time.                 ║
# ║                                                                     ║
# ╚═════════════════════════════════════════════════════════════════════╝

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numLen = len(nums)
        if numLen < 1:
            return 0
        nums.sort()

        print(nums)
        resultList = list()

        i = 1
        j = 0
        resultList.append([nums[0]])
        print(resultList)
        print(resultList[j][i-1])
        res = 0

        while i < numLen:
            print(i,j)
            if resultList[j][len(resultList[j])-1] == nums[i] - 1:
                resultList[j].append(nums[i])
            elif resultList[j][len(resultList[j])-1] == nums[i]:
                pass
            else:
                res = max(res,len(resultList[j]))
                resultList.append([nums[i]])
                j += 1
            i += 1

        print(resultList)
        return max(res, len(resultList[j]))

Wynik = Solution()

nums = [100,4,200,1,3,2]
Wynik1 = Wynik.longestConsecutive(nums=nums)
print("******\nWynik1", Wynik1, "\n******")

nums = [0,3,7,2,5,8,4,6,0,1]
Wynik1 = Wynik.longestConsecutive(nums=nums)
print("******\nWynik1", Wynik1, "\n******")

nums = [1,2,0,1]
Wynik1 = Wynik.longestConsecutive(nums=nums)
print("******\nWynik1", Wynik1, "\n******")
