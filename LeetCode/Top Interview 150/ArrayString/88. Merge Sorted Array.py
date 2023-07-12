class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        nums1 id() should be the same at the beginning and at the end
        """
        # print(nums1, id(nums1))
        # numsAux = nums1[:m]
        # print(nums1, id(nums1))
        # nums2 = nums2[:n]
        # numsAux += nums2
        # nums1 = numsAux
        # nums1.sort()
        # print(nums1, id(nums1))

        for i in range(m,m+n):
            nums1[i] = nums2[i-m]
            print(nums1, id(nums1))

        nums1.sort()
        print(nums1, id(nums1))
Wynik = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Wynik1 = Wynik.merge(nums1,m,nums2,n)

nums1 = [1]
m = 1
nums2 = []
n = 0
Wynik2 = Wynik.merge(nums1,m,nums2,n)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
Wynik3 = Wynik.merge(nums1,m,nums2,n)
