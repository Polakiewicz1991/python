# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitsStr = ''.join([str(x) for x in digits])
        # print(digitsStr)
        digitsInt = int(digitsStr)
        # print(digitsInt)
        digitsInt += 1
        digitsStr = str(digitsInt)
        digitsResult = [int(x) for x in digitsStr]
        # print(digitsResult)
        return digitsResult

Wynik = Solution()

digits = [4,3,2,1]
Wynik1 = Wynik.plusOne(digits=digits)
print("******\nWynik1", Wynik1, "\n******")