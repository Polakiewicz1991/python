# ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ Write an algorithm to determine if a number n is happy.                                                     ║
# ║                                                                                                             ║
# ║ A happy number is a number defined by the following process:                                                ║
# ║                                                                                                             ║
# ║    Starting with any positive integer, replace the number by the sum of the squares of its digits.          ║
# ║     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle     ║
# ║     which does not include 1.                                                                               ║
# ║     Those numbers for which this process ends in 1 are happy.                                               ║
# ║                                                                                                             ║
# ║ Return true if n is a happy number, and false if not.                                                       ║
# ║                                                                                                             ║
# ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

class Solution:
    def isHappy(self, n: int) -> bool:
        dec = 10
        num = []

        j = 0
        while n != 0:

            while n > 10:
                dec = 10
                # num.clear()
                if n > dec:
                    num.append(n % dec)
                    n = n // dec
                    print(n,num)
                j += 1
            num.append(n % dec)

            for i in range(len(num)):
                num[i] = num[i] * num[i]

            print(sum(num))
            n = sum(num)
            num.clear()

        return True

Wynik = Solution()

n = 19#532
Wynik1 = Wynik.isHappy(n=n)
print("******\nWynik1", Wynik1, "\n******")

n = 2
Wynik1 = Wynik.isHappy(n=n)
print("******\nWynik1", Wynik1, "\n******")