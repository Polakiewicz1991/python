# ╔═════════════════════════════════════════════════════════════════════╗
# ║ Given an integer array nums and an integer k,                       ║
# ║ return true if there are two distinct indices i and j in            ║
# ║ the array such that nums[i] == nums[j] and abs(i - j) <= k.         ║
# ║                                                                     ║
# ╚═════════════════════════════════════════════════════════════════════╝

from typing import List
class Solution:
    def containsNearbyDuplicateInternet(self, nums: List[int], k: int) -> bool:
        # Create hset for storing previous of k elements...
        hset = {}
        # Traverse for all elements of the given array in a for loop...
        for idx in range(len(nums)):
            # If duplicate element is present at distance less than equal to k, return true...
            if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
                return True
            hset[nums[idx]] = idx
        # If no duplicate element is found then return false...
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        windowLen = len(nums[0:k+1])

        if windowLen > len(set(nums[i:i+k+1])):
            return True
            i += 1

        while (i < len(nums) - k):
            print(nums[i:i+k+1])
            if windowLen > len(set(nums[i:i+k+1])):
                return True
            i += 1
        return False

Wynik = Solution()

nums = [1,2,3,1]
k = 3
Wynik1 = Wynik.containsNearbyDuplicate(nums=nums, k=k)
print("******\nWynik1", Wynik1, "\n******")

nums = [1,0,1,1]
k = 1
Wynik1 = Wynik.containsNearbyDuplicate(nums=nums, k=k)
print("******\nWynik1", Wynik1, "\n******")

nums = [1,2,3,1,2,3]
k = 2
Wynik1 = Wynik.containsNearbyDuplicate(nums=nums, k=k)
print("******\nWynik1", Wynik1, "\n******")

nums =[99,99]
k = 2
Wynik1 = Wynik.containsNearbyDuplicate(nums=nums, k=k)
print("******\nWynik1", Wynik1, "\n******")