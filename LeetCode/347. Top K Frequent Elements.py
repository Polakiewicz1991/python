import sys
from typing import List
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        setNums = set(nums)

        resultPaits = [0] * k
        pairNums = []

        for i in setNums:
            countNums = nums.count(i)
            pairNums.append((countNums, i))

        pairNums.sort()
        pairNums.reverse()

        for i in range(k):
            resultPaits[i] = pairNums[i][1]

        return resultPaits

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnums = collections.Counter(nums)
        print("cnums: ",cnums)
        print("[_[0] for _ in cnums.most_common()][:k]:",[_[0] for _ in cnums.most_common()][:k])
        return [_[0] for _ in cnums.most_common()][:k]

Wynik = Solution()
nums = [1,1,1,2,2,3,5,5,5,5,5,5]
k = 2
Wynik1 = Wynik.topKFrequent(nums= nums, k= k)
print("Wynik1: ",Wynik1)

nums = [1]
k = 1
Wynik2 = Wynik.topKFrequent(nums= nums, k= k)
print("Wynik2: ",Wynik2)
