class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # res = 0
        for i in nums:
            # print(nums.count(i))
            while (nums.count(i) > 1):
                nums.remove(i)
                # res += 1
        return len(nums)


Wynik = Solution()
nums1 = [1,1,2]
Wynik1 = Wynik.removeDuplicates(nums1)

nums1 = [0,0,1,1,1,2,2,3,3,4]
Wynik2 = Wynik.removeDuplicates(nums1)
print(Wynik1)
print(Wynik2)
#26. Remove Duplicates from Sorted Array
#27. Remove Element
#88. Merge Sorted Array
