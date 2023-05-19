class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pricesLen = len(prices)
        maxProfitVal = 0
        for i in range(pricesLen - 1):
            buy = prices[i]
            sell = max(prices[i+1:pricesLen])
            # print("buy:", buy, " sell:", sell)
            # print("buy - sell):", sell - buy)
            maxProfitVal = max(maxProfitVal,sell - buy)
        return maxProfitVal


    def maxProfit(self, prices: list[int]) -> int:
        maxProfitVal = 0
        lenProfit = len(prices)

        maxValSell = max(prices)
        maxIndex = prices.index(maxValSell)
        maxValBuy = min(prices[:maxIndex+1])
        maxVal = max(maxProfitVal,maxValSell - maxValBuy)
        print("prices[:maxIndex+1]:",prices[:maxIndex+1], " maxVal:", maxVal)


        minValBuy = min(prices)
        minIndex = prices.index(minValBuy)
        minValSell = max(prices[minIndex:])
        minVal = minValSell-minValBuy
        print("prices[minIndex:]:",prices[minIndex:], " minVal:", minVal)

        i = 1
        while i < lenProfit // 2:
            print("i:",i)
            maxValSell = max(prices[i:])
            maxIndex = prices.index(maxValSell)
            maxValBuy = min(prices[i:maxIndex + 1])
            maxVal = max(maxProfitVal, maxValSell - maxValBuy)
            print("prices[:maxIndex+1]:", prices[:maxIndex + 1], " maxVal:", maxVal)

            minValBuy = min(prices)
            minIndex = prices.index(minValBuy)
            minValSell = max(prices[minIndex:])
            minVal = minValSell - minValBuy
            print("prices[minIndex:]:", prices[minIndex:], " minVal:", minVal)

            i += 1

        maxProfitVal = max(maxProfitVal, maxValSell - maxValBuy,minValSell-minValBuy)

        return maxProfitVal

    def maxProfit(self, prices: list[int]) -> int:
        Val = 0
        maxProfitVal = 0
        lenProfit = len(prices)

        if lenProfit < 2:
            return 0

        Sell = max(prices[1:])
        sellIndex = prices.index(Sell)
        sellCount = prices.count(Sell)
        while sellCount > 1:
            sellIndex = prices[sellIndex + 1:].index(Sell) + 1
            sellCount = prices[sellIndex + 1:].count(Sell)
            print("sellCount: ",sellCount , " prices[sellIndex + 1:]:", prices[sellIndex + 1:])

        print("Sell:", Sell, " sellIndex:", sellIndex)
        if sellIndex > 0:
            Buy = min(prices[:sellIndex])
            Val = Sell - Buy
            print("Sell:", Sell, " sellIndex:", sellIndex, " Buy:", Buy, " Val:", Val)

        maxProfitVal = max(maxProfitVal, Val)

        return maxProfitVal

    def maxProfit(self, prices: list[int]) -> int:
        i = 0
        res = 0
        priscesLen = len(prices)
        print("prices:", prices)
        pricesReverse = list(reversed(prices))
        print("pricesReverse:",pricesReverse)

        while i < priscesLen/2:
            print("i:",i)
            sell = max(pricesReverse[:priscesLen - i])
            sellIndex = priscesLen - pricesReverse.index(sell) - 1

            buy = min(prices[i:])
            buyIndex = prices.index(buy)
            print("sell", sell, "buy", buy)
            print("sellIndex", sellIndex, "buyIndex", buyIndex)

            # res = max(res, sell - buy)
            print("res:", res)
            i += 1
            if sellIndex > buyIndex:
                res = max(res, sell - buy)

        return res
    def maxProfit(self, prices: list[int]) -> int:
        i = 0
        res = 0
        priscesLen = len(prices)

        # if priscesLen < 2:
        #     return 0

        while i < priscesLen:
            print("i:",i)
            print("prices[i:]:",prices[i:])
            maximum = max(prices[i:])
            print("maximum",maximum)
            maximumIndex = prices[i:].index(maximum) + i
            print("prices[i+1:]:", prices[i+1:])
            nextMaximum = max(prices[i+1:])
            print("nextMaximum",nextMaximum)
            if maximum == nextMaximum:
                nextMaximumIndex = prices[i+1:].index(nextMaximum) + i + 1
            else:
                nextMaximumIndex = prices[i:].index(nextMaximum) + i

            print("maximumIndex",maximumIndex,"nextMaximumIndex",nextMaximumIndex)
            i += nextMaximumIndex
            sell = max(prices[maximumIndex:])
            buy = min(prices[:nextMaximumIndex - 1])

            print(prices[maximumIndex:])
            print((prices[:nextMaximumIndex - 1]))

            sellIndex = prices[maximumIndex:].index(sell)
            buyIndex = prices[:nextMaximumIndex].index(buy)
            print("sell", sell, "sellIndex", sellIndex)
            print("buy", sell, "buyIndex", sellIndex)

            if sellIndex > buyIndex:
                res = max(res,sell - buy)

        return res

Wynik = Solution()
prices = [7,1,5,3,6,4]
print("Test: ",prices)
Wynik1 = Wynik.maxProfit(prices= prices) #5
print(Wynik1,"\n")

prices = [7,6,4,3,1]
print("Test: ",prices)
Wynik1 = Wynik.maxProfit(prices= prices) #0
print(Wynik1,"\n")

prices =[7,2,4,1]
print("Test: ",prices)
Wynik1 = Wynik.maxProfit(prices= prices) #2
print(Wynik1,"\n")

# prices =[1]
# print("Test: ",prices)
# Wynik1 = Wynik.maxProfit(prices= prices) #2
# print(Wynik1,"\n")
#
# prices =[3,3]
# print("Test: ",prices)
# Wynik1 = Wynik.maxProfit(prices= prices) #2
# print(Wynik1,"\n")

prices =[2,1,2,0,1]
print("Test: ",prices)
Wynik1 = Wynik.maxProfit(prices= prices) #2
print(Wynik1,"\n")

prices =[2,1,2,1,0,1,2]
print("Test: ",prices)
Wynik1 = Wynik.maxProfit(prices= prices) #2
print(Wynik1,"\n")