# ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ You are given a 0-indexed array nums of n integers, and an integer k.                                       ║
# ║                                                                                                             ║
# ║ The k-radius average for a subarray of nums centered at some index i with the radius k is the average       ║
# ║ of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements  ║
# ║ before or after the index i, then the k-radius average is -1.                                               ║
# ║                                                                                                             ║
# ║ Build and return an array avgs of length n where avgs[i]                                                    ║
# ║ is the k-radius average for the subarray centered at index i.                                               ║
# ║                                                                                                             ║
# ║ The average of x elements is the sum of the x elements divided by x, using integer division.                ║
# ║ The integer division truncates toward zero, which means losing its fractional part.                         ║
# ║                                                                                                             ║
# ║ For example, the average of four elements 2, 3, 1,                                                          ║
# ║ and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.                                         ║
# ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        numsLen = len(nums)
        i = k
        resList = [-1] * numsLen

        if numsLen < 2*k:
            return resList

        while i < numsLen:
            if i < k or i + k >= numsLen:
                pass
            else:
                # print(i, nums[i-k:i+k+1], sum(nums[i-k:i+k+1]), 2 * k + 1)
                resList[i] = sum(nums[i-k:i+k+1])//(2 * k + 1)
            i += 1

        return resList


Wynik = Solution()

nums = [7,4,3,9,1,8,5,2,6]
k = 3
# Output: [-1,-1,-1,5,4,4,-1,-1,-1]
Wynik1 = Wynik.getAverages(nums=nums, k=k)
print("******\nWynik1", Wynik1, "\n******")

nums = [100000]
k = 0
Wynik1 = Wynik.getAverages(nums=nums, k=k)
print("******\nWynik1", Wynik1, "\n******")

nums = [8]
k = 100000
Wynik1 = Wynik.getAverages(nums=nums, k=k)
print("******\nWynik1", Wynik1, "\n******")