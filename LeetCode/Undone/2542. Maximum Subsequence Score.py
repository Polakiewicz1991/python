from typing import List
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

    # Explanation:
    # Input: nums1 = [1, 3, 3, 2], nums2 = [2, 1, 3, 4], k = 3
    # The    four    possible    subsequence    scores    are:
    # - We    choose    the    indices    0, 1, and 2    with score = (1+3+3) * min(2, 1, 3) = 7.
    # - We    choose    the    indices    0, 1, and 3    with score = (1+3+2) * min(2, 1, 4) = 6.
    # - We    choose    the    indices    0, 2, and 3    with score = (1+3+2) * min(2, 3, 4) = 12.
    # - We    choose    the    indices    1, 2, and 3    with score = (3+3+2) * min(1, 3, 4) = 8.

    #   012345 ->   012 ->  013 ->  014 ->  015 ->  123 ->  124 ->  125 ->  234 ->  235 ->  245 ->  345
    #               0       1       2       3       4       5       6       7       8       9       10
    #   %4          0       1       2       3       0       1       2       3       0       1       2
    #   //4         0       0       0       0       1       1       1       1       2       2       2
    #   (//4+%4)%4  0       1       2       3       1       2       3       0       1       2       0
    #   (//4+%4)//4 0       0       0       0       0       0       0       1       0       0       0
    #               [0,1,2] [0,1,3] [0,1,4] [0,1,5] [1,2,3] [1,2,4] [1,2,5] [2,3,4] [0,3,5] [2,4,5]
    #   len: l = 6, k = 3, l + k - 1 = 4
    #   0   012
    #   1   013
    #   2   014
    #   3   015
    #   4   023
    #   5   024
    #   6   025
    #   7   034
    #   8   035
    #   9   045
    #   10  123
    #   11  124
    #   12  125
    #   13  134
    #   14  135
    #   15  145
    #   16  234
    #   17  245
    #   18  345


    #   //4+%4      0       1       2       3       1       2       3       4       6       2
    # Therefore, we    return the   max    score, which is 12.

        # indexes = [i for i in range(k)]
        # print(indexes)
        # numLen = len(nums1)
        # modulo = numLen
        # print("modulo: ",modulo)
        # i = 0
        # while i<18:
        #
        #         print(f"j: {j}, i: {i}", " indexes[j]:", indexes[j])
        #
        #         indexes[j] += 1
        #         if indexes[j] > modulo - 1:
        #             for j in range(k - 2, -1, -1):
        #                 indexes[j]
        #
        #     i += 1
        total = res = 0
        heap = []

        pairs = zip(nums1, nums2)

        sorted_pairs = sorted(pairs, key=lambda x: -x[1])

        for pair in sorted_pairs:
            num1, num2 = pair
            heappush(heap, num1)
            total += num1
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) == k:
                res = max(res, total * num2)

        return res
Wynik = Solution()
nums1 = [0,1,2,3,4,5]
nums2 = [1,2,1,3,4,1]
k = 3
Wynik1 = Wynik.maxScore(nums1= nums1, nums2= nums2, k= k)
print(Wynik1)


nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3
Wynik1 = Wynik.maxScore(nums1= nums1, nums2= nums2, k= k)
print(Wynik1)

nums1 = [4,2,3,1,1]
nums2 = [7,5,10,9,6]
k = 1
Wynik1 = Wynik.maxScore(nums1= nums1, nums2= nums2, k= k)
print(Wynik1)