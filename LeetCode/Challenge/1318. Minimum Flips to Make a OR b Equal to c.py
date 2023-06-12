class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        binA = format(a, 'b')
        binB = format(b, 'b')
        binC = format(c, 'b')
        res = 0
        print(binA, binB, binC , type(binA))
        while len(binA) < len(binC):
            binA = "0" + binA
        while len(binB) < len(binC):
            binB = "0" + binB

        print(binA, binB, binC, type(binA))
        for i, x in enumerate(binC):
            print(binA[i], binB[i], x)
            if (binA[i] == x or binB[i] == x):
                print(i, "True")
                continue
            else:
                print(i, "False")
                if binA[i] != x:
                    # binA[i] = x
                    res += 1
                if binB[i] != x:
                    # binB[i] = x
                    res += 1
        return res

Wynik = Solution()

a = 2
b = 6
c = 5
Wynik1 = Wynik.minFlips(a=a, b=b, c=c)
print("******\nWynik1", Wynik1, "\n******")