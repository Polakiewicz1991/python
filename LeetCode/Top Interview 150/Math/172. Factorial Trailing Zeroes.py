# Given an integer n, return the number of trailing zeroes in n!.
#
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

class Solution:
    def trailingZeroes1(self, n: int) -> int:
        def silnia(n):
            if n == 0:
                return 1
            else:
                return n * silnia(n - 1)

        print(silnia(n))
        silniaStr = str(silnia(n))

        n = 0
        while n < len(silniaStr):
            if silniaStr[-1 - n] == "0":
                n += 1
            else:
                return n
        return n

    def trailingZeroes(self, n: int) -> int:
        def silnia(n):
            if n == 0:
                return 1
            else:
                return n * silnia(n - 1)

        silniaN = (silnia(n))
        n = 0
        # print(silniaN)
        while silniaN % 10 == 0 and silniaN != 0:
            # print("silniaN % 10: ",silniaN % 10)
            silniaN = silniaN // 10
            # print("silniaN",silniaN)

            n += 1

        return n

    def trailingZeroes(self, n):
        #Kod działa ponieważ, aby określić ilość 0 na końcu mnożenia najważniejsza jest mnożenie przez 2 i 5
        #dlatego sprawdzana jest ilość potę liczby 5 zawierająca się w zmiennej "n"
        # Negative Number Edge Case
        if(n < 0):
            return -1
        # Initialize output...
        output = 0
        # Keep dividing n by 5 & update output...
        while(n >= 5):
            n //= 5
            output += n
        return output    # Return the output...


Wynik = Solution()

n = 5
Wynik1 = Wynik.trailingZeroes(n=n)
print("******\nWynik1", Wynik1, "\n******")

n = 6
Wynik1 = Wynik.trailingZeroes(n=n)
print("******\nWynik1", Wynik1, "\n******")

n = 7
Wynik1 = Wynik.trailingZeroes(n=n)
print("******\nWynik1", Wynik1, "\n******")

n = 8123
Wynik1 = Wynik.trailingZeroes(n=n)
print("******\nWynik1", Wynik1, "\n******")