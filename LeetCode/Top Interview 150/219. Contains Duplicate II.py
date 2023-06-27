# ╔═════════════════════════════════════════════════════════════════════╗
# ║ Given an integer array nums and an integer k,                       ║
# ║ return true if there are two distinct indices i and j in            ║
# ║ the array such that nums[i] == nums[j] and abs(i - j) <= k.         ║
# ║                                                                     ║
# ╚═════════════════════════════════════════════════════════════════════╝

from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pass

Wynik = Solution()

nums = [1,2,3,1]
k = 3
Wynik1 = Wynik.containsNearbyDuplicate(nums=nums, k=k)
print("******\nWynik1", Wynik1, "\n******")


