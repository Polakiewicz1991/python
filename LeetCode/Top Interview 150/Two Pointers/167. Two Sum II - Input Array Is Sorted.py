from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for n in numbers:
            if (target - n) in numbers:
                return [numbers.index(n) + 1,numbers[numbers.index(n) + 1:].index(target - n) + numbers.index(n) + 1 + 1]


Wynik = Solution()
numbers = [2,7,11,15]
target = 9
Wynik1 = Wynik.twoSum(numbers= numbers, target= target)
print("Wynik1", Wynik1)

numbers = [2,3,4]
target = 6
Wynik1 = Wynik.twoSum(numbers= numbers, target= target)
print("Wynik1", Wynik1)

numbers = [0,0,3,4]
target = 0
Wynik1 = Wynik.twoSum(numbers= numbers, target= target)
print("Wynik1", Wynik1)