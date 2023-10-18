class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x

        divX = x // 2

        while (divX) * (divX) >= (x):
            print("(divX + 1) * (divX + 1):", (divX + 1) * (divX + 1))
            print("divX:", divX)
            # if (divX) * (divX) > 2*x:
            divX = divX // 2
            # else:
            #     divX = divX - 1

        while (divX + 1) * (divX + 1) <= x:
            divX = divX + 1

        return divX

Wynik = Solution()

x = 1
print("\n\nx=",x)
Wynik1 = Wynik.mySqrt(x=x)
print("******\nWynik1", Wynik1, "\n******")

x = 183692038
print("\n\nx=",x)
Wynik1 = Wynik.mySqrt(x=x) #13553
print("******\nWynik1", Wynik1, "\n******")

x = 16
print("\n\nx=",x)
Wynik1 = Wynik.mySqrt(x=x)
print("******\nWynik1", Wynik1, "\n******")

x = 8
print("\n\nx=",x)
Wynik1 = Wynik.mySqrt(x=x)
print("******\nWynik1", Wynik1, "\n******")

x = 6
print("\n\nx=",x)
Wynik1 = Wynik.mySqrt(x=x)
print("******\nWynik1", Wynik1, "\n******")