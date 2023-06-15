# ╔═════════════════════════════════════════════════════╗
# ║ Czy podana lista jest ułożona w sposób artmetyczny: ║
# ╚═════════════════════════════════════════════════════╝
from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        y = arr[0]
        step = y - arr[1]

        for x in range(1,len(arr)):
            # print(x, " step", step, " y - x:", y - arr[x])
            if y - arr[x] != step:
                return False
            step = y - arr[x]
            y = arr[x]

        return True

Wynik = Solution()

arr = [3,5,1]
Wynik1 = Wynik.canMakeArithmeticProgression(arr= arr)
print("******\nWynik1", Wynik1, "\n******")

arr = [1,2,4]
Wynik1 = Wynik.canMakeArithmeticProgression(arr= arr)
print("******\nWynik1", Wynik1, "\n******")