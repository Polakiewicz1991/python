import sys


class Solution:
    def reverse(self, x: int) -> int:
        i = 1

        xInt = abs(x)
        if x >= i:
            iSign = 1
        else:
            iSign = -1

        #print("xInt: ",xInt )
        iResult = 0
        while (i) <= abs(x):
            i = i * 10
            xModulo = xInt % 10
            xInt = xInt // 10
            #xInt = xRest
            # print("i: ",i)
            iResult = iResult * 10 + xModulo
            # print(xModulo)
            # print(xRest)
            # print("iResult: ",iResult)
            if iResult > 2**31 - 1:
                return 0

        return iResult * iSign

    def reverse2(self, x: int) -> int:
        intMax = 2 ** 31 - 1
        intMin = -1 * 2 ** 31
        xStr = str(x) if x >= 0 else str(x)[1:]
        print("xStr: ",xStr)
        xRev = xStr[::-1] if x >= 0 else '-' + xStr[::-1]
        print("xRev: ",xRev)
        xRevInt = int(xRev)
        if xRevInt > intMax or xRevInt < intMin:
            return 0
        return xRevInt

Wynik = Solution()
# print(Wynik.reverse(-4563212332132131215245342544654365429999999999999321))
print(Wynik.reverse2(-4563212))
# print("sys.maxsize: ",sys.maxsize)
