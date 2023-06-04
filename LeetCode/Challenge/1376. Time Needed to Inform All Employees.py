import sys


class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        sorted_managers = sorted(enumerate(manager), key=lambda x: x[1])
        employee_power = -sys.maxsize
        total_time = 0
        for i, employee in sorted_managers:
            if employee > employee_power:
                total_time += informTime[i]
                employee_power = employee
            print(f"{i} {employee}")

        return total_time

Wynik = Solution()
n = 1
headID = 0
manager = [-1]
informTime = [0]
Wynik1 = Wynik.numOfMinutes(n= n, headID= headID, manager= manager, informTime= informTime)
print("\n*****\nWynik1:", Wynik1, "\n*****\n")

n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]
Wynik1 = Wynik.numOfMinutes(n= n, headID= headID, manager= manager, informTime= informTime)
print("\n*****\nWynik1:", Wynik1, "\n*****\n")

n = 7
headID = 6
manager = [1,2,3,4,5,6,-1]
informTime = [0,6,5,4,3,2,1] #1+2+6+5+4+3
Wynik1 = Wynik.numOfMinutes(n= n, headID= headID, manager= manager, informTime= informTime)
print("\n*****\nWynik1:", Wynik1, "\n*****\n") # 21

n = 15
headID = 0
manager =       [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
informTime =    [1 ,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
Wynik1 = Wynik.numOfMinutes(n= n, headID= headID, manager= manager, informTime= informTime)
print("\n*****\nWynik1:", Wynik1, "\n*****\n") # 3