from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if target in nums:
            return 1

        nums.sort()
        nums.reverse()
        nums = list(filter(lambda x: x < target, nums))
        maxVal = max(nums)
        res = target - maxVal
        def dp(nums,res):
            if res in nums:
                return 1
            maxVal = max(nums)
            nums = list(filter(lambda x: x < res, nums))
            dp(nums,res)
            # while maxVal > target:
            #     nums.remove(maxVal)
            maxVal = max(nums)

            print(nums)
            print(target - maxVal)
            res = 0


        # if target - maxVal in nums:
        #     #target - maxVal = 1
        #     #target -








Wynik = Solution()

target = 7
nums = [2,3,1,2,4,3]
Wynik1 = Wynik.minSubArrayLen(target=target,nums=nums)
print("******\nWynik1", Wynik1, "\n******")

target = 8
nums = [1,3,1,1,4,3,6,11,9,10]
Wynik1 = Wynik.minSubArrayLen(target=target,nums=nums)
print("******\nWynik1", Wynik1, "\n******")