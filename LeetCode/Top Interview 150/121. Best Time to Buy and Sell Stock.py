class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pricesLen = len(prices)
        maxProfitVal = 0
        res = 0
        for i in range(pricesLen - 1):
            print(prices[i+1:pricesLen],min(prices[i+1:pricesLen]))
            if min(prices[i+1:pricesLen]) > maxProfitVal:
                maxProfitVal = min(prices[i + 1:pricesLen])
                res = i

            print("res: ", maxProfitVal)
        return maxProfitVal

Wynik = Solution()
prices = [7,1,5,3,6,4]
Wynik1 = Wynik.maxProfit(prices= prices) #5
print(Wynik1,"\n")

prices = [7,6,4,3,1]
Wynik1 = Wynik.maxProfit(prices= prices) #0
print(Wynik1,"\n")