class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        numSum = nums1 + nums2
        numSum.sort()

        # print(numSum)

        numSumLenght = len(numSum)
        numSumMid = (numSumLenght//2)

        # print("numSumLenght: ",numSumLenght)
        # print("numSumMi: ",numSumMid)
        # print("numSumLenght % 2 == 0:",numSumLenght % 2 == 0)

        if numSumLenght % 2 == 0:
            return (numSum[numSumMid - 1] + numSum[numSumMid])/2
        else:
            return numSum[numSumMid]


Wynik = Solution()
print(Wynik.findMedianSortedArrays([1,2,3,4,5],[6,6,6,6,2,3]))
