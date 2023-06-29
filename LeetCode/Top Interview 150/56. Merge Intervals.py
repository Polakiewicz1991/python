# ╔═════════════════════════════════════════════════════════════════════════════════╗
# ║ Given an array of intervals where intervals[i] = [starti, endi],                ║
# ║ merge all overlapping intervals, and return an array of the non-overlapping     ║
# ║ intervals that cover all the intervals in the input.                            ║
# ║                                                                                 ║
# ╚═════════════════════════════════════════════════════════════════════════════════╝


from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 1

        resList =  list([intervals[0]])
        while i < len(intervals):
            # print(i, "resList[len(resList)-1][1]:", resList[len(resList)-1][1], "intervals[i-1][0]", intervals[i-1][0])
            if resList[len(resList) - 1][0] > intervals[i][0]:
                resList[len(resList) - 1][0] = intervals[i][0]

            if resList[len(resList)-1][1] >= intervals[i][0]:
                resList[len(resList)-1][1] = intervals[i][1]

            else:
                resList.append(intervals[i])

            i += 1

        # print(resList)
        return resList

Wynik = Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]
Wynik1 = Wynik.merge(intervals=intervals)
print("******\nWynik1", Wynik1, "\n******")

intervals = [[1,4],[4,5]]
Wynik1 = Wynik.merge(intervals=intervals)
print("******\nWynik1", Wynik1, "\n******")

intervals = [[1,4],[0,4]]
Wynik1 = Wynik.merge(intervals=intervals)
print("******\nWynik1", Wynik1, "\n******")
