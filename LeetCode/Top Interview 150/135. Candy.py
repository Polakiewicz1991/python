from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candyList = [1] * len(ratings)

        for kid in range(1,len(ratings)):
            print(kid)
            if ratings[kid - 1] > ratings[kid] and candyList[kid - 1] <= candyList[kid]:
                candyList[kid - 1] += 1

            if ratings[kid] > ratings[kid - 1]: #and candyList[kid] <= candyList[kid - 1]:
                candyList[kid] += 1
                if candyList[kid] >= candyList[kid - 1]:
                    candyList[kid] += 1

            print("ratings      ", ratings)
            print("candyList    ", candyList)
        return sum(candyList)
    def candy(self, ratings: List[int]) -> int:
        candyList = [1] * len(ratings)

        for i in range(len(ratings)-1):
            j = len(ratings) - 1 - i

            if ratings[i + 1] > ratings[i] and candyList[i + 1] <= candyList[i]:
                candyList[i + 1] = candyList[i] + 1
            if ratings[j - 1] > ratings[j]  and candyList[j - 1] <= candyList[j]:
                candyList[j - 1] = candyList[j] + 1

        return sum(candyList)
Wynik = Solution()
ratings = [1,0,2]
Wynik1 = Wynik.candy(ratings= ratings)
print("Wynik1: ", Wynik1)

ratings = [1,2,2]
Wynik1 = Wynik.candy(ratings= ratings)
print("Wynik1: ", Wynik1)

ratings = [1,3,2,2,1]
Wynik1 = Wynik.candy(ratings= ratings)
print("Wynik1: ", Wynik1)

ratings = [1,2,87,87,87,2,1]
Wynik1 = Wynik.candy(ratings= ratings)
print("Wynik1: ", Wynik1)

ratings = [1,2,3,5,4,3,2,1,4,3,2,1]
Wynik1 = Wynik.candy(ratings= ratings)
print("Wynik1: ", Wynik1)