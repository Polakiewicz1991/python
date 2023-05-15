class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:

        i = 0
        result = 0
        while i < len(nums1):
            j = i
            # print("i: ", i, " j: ", j)
            while j < len(nums2):
                if nums1[i] == nums2[j]:
                    print("i: ", i ," j: ", j)
                    result += 1

                j += 1
            i += 1
        return result
Wynik = Solution()
print(Wynik.maxUncrossedLines([1,4,2],[1,2,4]))

print(Wynik.maxUncrossedLines([2,5,1,2,5],[10,5,2,1,5,2]))