# ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ Given an array of integers nums and an integer target, return indices of the two numbers                    ║
# ║ such that they add up to target.                                                                            ║
# ║                                                                                                             ║
# ║ You may assume that each input would have exactly one solution, and you may not use the same element twice. ║
# ║                                                                                                             ║
# ║ You can return the answer in any order.                                                                     ║
# ║                                                                                                             ║
# ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):
            if target-num in nums:
                if nums.index(target-num) != i:
                    return [i,nums.index(target-num)]

Wynik = Solution()

nums = [2,7,11,15]
target = 9
Wynik1 = Wynik.twoSum(nums=nums,target=target)
print("******\nWynik1", Wynik1, "\n******")

nums = [3,2,4]
target = 6
Wynik1 = Wynik.twoSum(nums=nums,target=target)
print("******\nWynik1", Wynik1, "\n******")