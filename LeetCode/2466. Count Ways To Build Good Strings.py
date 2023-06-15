class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        addZero = '0' * zero
        addOne = '1' * one
        strResult = ''
        strResultFilter = []
        print("addZero: ",addZero," addOne: ",addOne,)

        def addString(addStr,strResult,):
            if high < (len(strResult)): return
            strResult +=  addStr
            print("strResult: ",strResult)
            if (len(strResult) >= low) and (len(strResult) <= high): strResultFilter.append(strResult)
            print("strResultFilter: ",strResultFilter)
            addString(addZero, strResult)
            addString(addOne, strResult)

        addString(addZero,strResult)
        addString(addOne, strResult)
        return len(strResultFilter)

    # def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
    #     addZero = '0' * zero
    #     addOne = '1' * one
    #     strResult = ''
    #     strResultFilter = []
    #     # print("addZero: ",addZero," addOne: ",addOne,)
    #
    #     def addString(addStr,strResult):
    #         if high  < len(strResult): return
    #         strResult +=  addStr
    #         if (len(strResult) >= low) and (len(strResult) <= high): strResultFilter.append(strResult)
    #         addString(addZero,strResult)
    #         addString(addOne,strResult)
    #
    #     addString(addZero,strResult)
    #     addString(addOne, strResult)
    #     return len(strResultFilter)



Wynik = Solution()
Wynik1 = Wynik.countGoodStrings(2,3,1,2)
Wynik2 = Wynik.countGoodStrings(3,3,1,1)
Wynik3 = Wynik.countGoodStrings(10,10,2,1)
Wynik4 = Wynik.countGoodStrings(200,200,10,1)

print("Wynik1: ",Wynik1)
print("Wynik2: ",Wynik2)
print("Wynik3: ",Wynik3)
print("Wynik4: ",Wynik4)