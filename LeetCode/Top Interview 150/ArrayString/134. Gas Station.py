from typing import List, Optional

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        routeLen = len(gas)
        costToGet = [0] * routeLen
        travel = 0

        if routeLen == 1:
            if gas[0] - cost[0] >= 0:
                return 0
            else:
                return -1

        for i in range(routeLen):
            j = (i + 1) % routeLen
            costToGet[i] = gas[i] - cost[i]
            sum = 0
            if gas[i] - cost[i] > 0:
                for x1 in range(routeLen):
                    x2 = (x1 + i) % routeLen
                    sum += gas[x2] - cost[x2]
                    print("x2:", x2, "sum:", sum)
                    if sum < 0:
                        break
                    if x1 == routeLen - 1:
                        return i
        return -1

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas = [1, 2, 3, 4, 5]   cost = [3, 4, 5, 1, 2]
        # Travel        to        station        4.        Your        tank = 4 - 1 + 5 = 8
        # Travel        to        station        0.        Your        tank = 8 - 2 + 1 = 7
        # Travel        to        station        1.        Your        tank = 7 - 3 + 2 = 6
        # Travel        to        station        2.        Your        tank = 6 - 4 + 3 = 5

        routeLen = len(gas)
        costToGet = list(map(lambda x, y: x - y, gas, cost))
        resultList = [True] * routeLen
        resultList = list(map(lambda x, y: (x >= 0) and y, costToGet, resultList))
        costResult = costToGet.copy()
        # print("costToGet",costToGet)
        shiftCostToGet = costToGet[1:routeLen] + [costToGet[0]]
        # print("shiftCostToGet",shiftCostToGet)
        for i in range(routeLen - 1):
            costResult = list(map(lambda x, y: x + y, costResult, shiftCostToGet))
            shiftCostToGet = shiftCostToGet[1:routeLen] + [shiftCostToGet[0]]
            resultList = list(map(lambda x, y: (x >= 0) and y, costResult, resultList))
            # print("shiftCostToGet", shiftCostToGet)
            # print("costResult",costResult)
            # print("resultList:",resultList)
        if True in resultList:
            return resultList.index(True)
        else:
            return -1
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas = [1, 2, 3, 4, 5]   cost = [3, 4, 5, 1, 2]
        # Travel        to        station        4.        Your        tank = 4 - 1 + 5 = 8
        # Travel        to        station        0.        Your        tank = 8 - 2 + 1 = 7
        # Travel        to        station        1.        Your        tank = 7 - 3 + 2 = 6
        # Travel        to        station        2.        Your        tank = 6 - 4 + 3 = 5
        def productExceptSelf(nums: List[int]) -> List[int]:
            length = len(nums)
            #sol = [0] * length
            sol = nums.copy()
            print("sol",sol)
            pre = 0
            post = 0
            for i in range(length):
                sol[i] += pre
                pre = pre + nums[i]
                sol[length - i - 1] += post
                post = post + nums[length - i - 1]

                print("pre", pre, " post", post)
            return (sol)

        routeLen = len(gas)
        costToGet = list(map(lambda x, y: x - y, gas, cost))
        costResult = costToGet.copy()
        print("costToGet",costToGet)
        costResult = productExceptSelf(costToGet)
        print("costResult", costResult)
        shiftCostToGet = costToGet[1:routeLen] + [costToGet[0]]
        # print("shiftCostToGet",shiftCostToGet)
        # for i in range(routeLen - 1):
        print("shiftCostToGet",costResult)
        costResult = list(map(lambda x, y: x + y, costResult, shiftCostToGet))
        print("shiftCostToGet", costResult)
        maxCost= max(costResult)
        print(maxCost)
        if maxCost > 0:
            return costResult.index(maxCost)
        else:
            return -1

    def canCompleteCircuitInternet(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        res, total = 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
        return res



Wynik = Solution()

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
Wynik1 = Wynik.canCompleteCircuit(gas= gas, cost= cost)
print("Wynik1: ",Wynik1)

gas = [2,3,4]
cost = [3,4,3]
Wynik2 = Wynik.canCompleteCircuit(gas= gas, cost= cost)
print("Wynik2: ",Wynik2)

gas = [2]
cost = [3]
Wynik3 = Wynik.canCompleteCircuit(gas= gas, cost= cost)
print("Wynik3: ",Wynik3)

gas = [4,5,2,6,5,3]
cost = [3,2,7,3,2,9]
Wynik4 = Wynik.canCompleteCircuit(gas= gas, cost= cost)
print("Wynik4: ",Wynik4)