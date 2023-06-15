from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations.reverse()
        print(citations)
        res = 0
        while True:
            if citations[res] > res:
                res += 1
            else:
                return res


Wynik = Solution()
citations = [3,0,6,1,5]
Wynik1 = Wynik.hIndex(citations)
print("Wynik1: ", Wynik1)

citations = [1,3,1]
Wynik2 = Wynik.hIndex(citations)
print("Wynik2: ", Wynik2)
