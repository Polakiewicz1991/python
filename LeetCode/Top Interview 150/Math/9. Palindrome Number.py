class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        n = 0
        # print(xStr)
        # print(xStr[n])
        # print(xStr[-1 - n])
        while n <= len(xStr)/2:
            if xStr[n] == xStr[-1 -n]:
                n += 1
                continue
            else:
                return False

        return True

Wynik = Solution()

x = 121
Wynik1 = Wynik.isPalindrome(x=x)
print("******\nWynik1", Wynik1, "\n******")

x = -121
Wynik1 = Wynik.isPalindrome(x=x)
print("******\nWynik1", Wynik1, "\n******")

# x = 10
Wynik1 = Wynik.isPalindrome(x=x)
print("******\nWynik1", Wynik1, "\n******")
