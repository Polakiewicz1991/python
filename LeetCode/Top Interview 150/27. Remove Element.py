class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        # print("nums",nums)
        return len(nums)

Wynik = Solution()
nums1 = [3,2,2,3]
Wynik1 = Wynik.removeElement(nums1,3)

nums1 = [0,1,2,2,3,0,4,2]
Wynik2 = Wynik.removeElement(nums1,2)

print(Wynik2,nums1)
