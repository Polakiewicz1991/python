# ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]               ║
# ║ represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.       ║
# ║ You are also given an interval newInterval = [start, end] that represents the start and end of another interval.║
# ║                                                                                                                 ║
# ║ Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals║
# ║ still does not have any overlapping intervals (merge overlapping intervals if necessary).                       ║
# ║                                                                                                                 ║
# ║ Return intervals after the insertion.                                                                           ║
# ║                                                                                                                 ║
# ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

from typing import List


class Solution:
    def insert3(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) > 0:
            resList =  list([intervals[0]])
        else:
            return [newInterval]

        if newInterval[0] >= resList[0][0] and newInterval[0] <= resList[0][1]:
            if newInterval[1] >= resList[0][1]:
                resList[0][1] = newInterval[1]

        if intervals[0][0] >= resList[0][0] and intervals[0][0] <= resList[0][1]:
            if intervals[0][1] >= resList[0][1]:
                resList[0][1] = intervals[0][1]

        i = 1
        while i < len(intervals):
            lastIndex = len(resList) - 1

            print(i)
            print(newInterval[0] >= resList[lastIndex][0], newInterval[0], resList[lastIndex][0])
            print(newInterval[0] <= resList[lastIndex][1], newInterval[0], resList[lastIndex][1])
            print(intervals[i][0] <= newInterval[1], intervals[i][0], newInterval[1])

            if newInterval[0] >= resList[lastIndex][0] and newInterval[0] <= resList[lastIndex][1]:
                if newInterval[1] >= resList[lastIndex][1]:
                    resList[lastIndex][1] = newInterval[1]

            if intervals[i][0] >= resList[lastIndex][0] and intervals[i][0] <= resList[lastIndex][1]:
                if intervals[i][1] >= resList[lastIndex][1]:
                    resList[lastIndex][1] = intervals[i][1]
            else:
                resList.append(intervals[i])
            print(resList, intervals[i])
            i += 1

        lastIndex = len(resList) - 1
        if newInterval[0] >= resList[lastIndex][1]:
            resList.append(newInterval)

        return resList

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) > 0:
            resList =  list()
        else:
            return [newInterval]

        for x in intervals:
            # print(x)
            if x[0] < newInterval[0] or x[1] > newInterval[1]:
                resList.append(x)

            lastIndex = len(resList) - 1
            if newInterval[0] >= resList[lastIndex][0] and newInterval[0] <= resList[lastIndex][1]:
                if newInterval[1] >= resList[lastIndex][1]:
                    resList[lastIndex][1] = newInterval[1]

            print(x, x[0] >= resList[lastIndex][0] and x[0] <= resList[lastIndex][1])
            if x[0] >= resList[lastIndex][0] and x[0] <= resList[lastIndex][1]:
                if x[1] >= resList[lastIndex][1]:
                    resList[lastIndex][1] = x[1]

        return resList

Wynik = Solution()

intervals = [[1,3],[6,9]]
newInterval = [2,5]
Wynik1 = Wynik.insert(intervals=intervals,newInterval=newInterval)
print("******\nWynik1", Wynik1, "\n******")

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
Wynik1 = Wynik.insert(intervals=intervals,newInterval=newInterval)
print("******\nWynik1", Wynik1, "\n******")

intervals =[[1,5]]
newInterval =[2,7]
Wynik1 = Wynik.insert(intervals=intervals,newInterval=newInterval)
print("******\nWynik1", Wynik1, "\n******")

intervals =[[1,5]]
newInterval =[6,8]
Wynik1 = Wynik.insert(intervals=intervals,newInterval=newInterval)
print("******\nWynik1", Wynik1, "\n******")
