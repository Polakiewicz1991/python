import sys


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        def parProfit(prices: list[int], pricesPar: list = []) -> int:
            i = 0
            m = sys.maxsize
            maxProfit = 0
            res = 0
            while True:
                if prices[i] < m:
                    m = prices[i]
                    mi = i

                profit = prices[i] - m


                if profit > maxProfit:
                    pricesPar.append(prices[mi: i + 1])
                    prices = prices[0:mi] + prices[i+1:]
                    print("pricesPar",pricesPar," mi:", mi, " i: ", i)
                    print("prices",prices)
                    i = 0
                    m = sys.maxsize
                else:
                    i += 1

                maxProfit = max(maxProfit, profit)

                pricesLen = len(prices)
                if i >= pricesLen:
                    for price in pricesPar:
                        res += max(price) - min(price)
                    return res

        pricesLen = len(prices)
        res = 0

        print(prices)
        res = max(res,parProfit(prices= prices))
        return res

    def maxProfit2(self, prices: list[int]) -> int:
        ans = 0
        x = prices[0]
        for i in range(1, len(prices)):
            print("i: ", i, " x:", x, " prices[i]:", prices[i], " ans: ", ans)
            if (x > prices[i]):
                x = prices[i]
            else:
                ans += prices[i] - x
                x = prices[i]
        return ans

Wynik = Solution()
prices = [7,1,5,3,6,4]
print("Test: ",prices)
Wynik1 = Wynik.maxProfit(prices= prices) #5
print(Wynik1,"\n")


prices = [1,2,3,4,5]
print("Test: ",prices)
Wynik2 = Wynik.maxProfit(prices= prices) #5
print(Wynik2,"\n")
# Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.