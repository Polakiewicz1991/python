from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resNums = [1] * len(nums)

        for i in range(1,len(nums) + 1):

            # print("i:", i)
            # print("resNums[:i]", resNums[:i-1])
            # print("resNums[i:]:", nums[i-1:i])
            # print("resNums[i:]:",resNums[i:])
            resNumsRest = nums[:i - 1] + nums[i:]
            # print("resNumsRest", resNumsRest)
            resNumsRest.remove(1)
            numNr = 0

            for x in resNumsRest:
                # print(x)
                resNums[i-1] = resNums[i-1] * x
                # print("resNums", resNums)
        return resNums

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        sol = [1] * length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre * nums[i]
            sol[length - i - 1] *= post
            post = post * nums[length - i - 1]
            print(sol)
        return (sol)
Wynik = Solution()

nums = [1,2,3,4]
print("nums: ",nums)
Wynik1 = Wynik.productExceptSelf(nums= nums)
print("wynik1: ",Wynik1)

nums = [-1,1,0,-3,3]
print("nums: ",nums)
Wynik1 = Wynik.productExceptSelf(nums= nums)
print("wynik1: ",Wynik1)