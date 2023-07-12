class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsAux = nums.copy()
        numLen = len(nums)
        k = k % numLen
        # print("numLen:",numLen," k:",k," numsAux:",numsAux)
        for i in range(numLen):
            if i + k >= numLen:
                # nums[i] = numsAux[(i + k) - numLen - 1]
                print("(i + k) - numLen:", (i + k) - numLen, " i:", i)
                nums[(i + k) - numLen] = numsAux[i]
            if i + k < numLen:
                # nums[i] = numsAux[i + k]
                # print("i + k:",i + k," i:",i)
                print("nums[i + k]: ",nums[i + k],"numsAux[i]: ",numsAux[i])
                nums[i + k] = numsAux[i]
            # print(nums)
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsAux = nums.copy()
        numLen = len(nums)
        k = k % numLen
        for i in range(numLen):
            if i + k >= numLen:
                nums[(i + k) - numLen] = numsAux[i]
            if i + k < numLen:
                nums[i + k] = numsAux[i]

Wynik = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
Wynik1 = Wynik.rotate(nums=nums,k=k)
print(nums,"\n")

nums = [-1,-100,3,99]
k = 2
Wynik2 = Wynik.rotate(nums=nums,k=k)
print(nums,"\n")

nums = [-1]
k = 2
Wynik3 = Wynik.rotate(nums=nums,k=k)
print(nums,"\n")


