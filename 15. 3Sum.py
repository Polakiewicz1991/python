class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        resultList = set()
        nums.sort()
        # print("len(nums): ",len(nums))
        if len(nums) >= 3:
            i = 0
            while i <= len(nums) - 3:
                j = i + 1
                while j <= len(nums) - 2:
                    k = j + 1
                    numsSum = 0

                    while k <= len(nums) - 1:
                        numsSum = nums[i] + nums[j] + nums[k]
                        # print("numsSum: ", numsSum)
                        if numsSum == 0:
                            auxLust = (nums[i],nums[j],nums[k])
                            # auxLust.sort()
                            print("auxLust: ",auxLust)
                            # if resultList.count(auxLust) == 0:
                            resultList.add(tuple(auxLust))
                            # resultList += ([nums[i],nums[j],nums[k]])
                        k += 1
                        # print(numsSum)
                    j += 1
                i += 1

            return list(resultList)
        else:
            return  []
    def threeSum2(self, nums: list[int]) -> list[list[int]]:
        resultList = set()
        nums.sort()
        i = 0
        j = len(nums) - 1
        # print("len(nums): ",len(nums))
        if len(nums) >= 3:
            while j >= i:
                while i <= j:
                    numsSum = nums[i] + nums[j]
                    try:
                        k = nums.index(-numsSum)
                        print("i: ", i,"j: ", j,"k: ", k)
                        print("[nums[i],nums[j],nums[k]]:",[nums[i],nums[j],nums[k]])
                        if k != i and k != j and i != j:
                            auxLust = [nums[i],nums[j],nums[k]]
                            auxLust.sort()
                            print("auxLust: ",auxLust)
                            resultList.add(tuple(auxLust))
                            # resultList.add(list(auxLust))
                    except:
                        pass

                    i += 1

                j -= 1
                i = 0

            return list(resultList)
        else:
            return  []

    def threeSum3(self, nums: list[int]) -> list[list[int]]:

        res = set()

        # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        # 2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))

        # 3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0, 0, 0))

        # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        return res

def threeSumClosest(self, nums: list[int], target: int) -> int:
    res = set()

    # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
    n, p, z = [], [], []
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)

    # 2. Create a separate set for negatives and positives for O(1) look-up times
    N, P = set(n), set(p)

    # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
    #   i.e. (-3, 0, 3) = 0
    if z:
        for num in P:
            if -1 * num in N:
                res.add((-1 * num, 0, num))

    # 3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
    if len(z) >= 3:
        res.add((0, 0, 0))

    # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
    #   exists in the positive number set
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            target = -1 * (n[i] + n[j])
            if target in P:
                res.add(tuple(sorted([n[i], n[j], target])))

    # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
    #   exists in the negative number set
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            target = -1 * (p[i] + p[j])
            if target in N:
                res.add(tuple(sorted([p[i], p[j], target])))

    return res


Wynik = Solution()
# print("Wynik: ",Wynik.threeSum2([-1,0,1,2,-1,-4]))

print("Wynik: ",Wynik.threeSum3([34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]))