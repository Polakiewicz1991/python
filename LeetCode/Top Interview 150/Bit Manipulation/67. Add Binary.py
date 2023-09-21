# ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ Given two binary strings a and b, return their sum as a binary string.                                          ║
# ║                                                                                                                 ║
# ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = int(a,2) + int(b,2)
        res = bin(res)
        
        return res[2:]
Wynik = Solution()

a = "11"
b = "1"
Wynik1 = Wynik.addBinary(a=a, b=b)
print("******\nWynik1", Wynik1, "\n******")

a = "1010"
b = "1011"
Wynik1 = Wynik.addBinary(a=a, b=b)
print("******\nWynik1", Wynik1, "\n******")