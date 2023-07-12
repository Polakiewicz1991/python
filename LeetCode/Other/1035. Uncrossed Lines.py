class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        resultat = 0
        last = [0,len(nums2)]
        resultList = []
        auxList = []
        for n1 in enumerate(nums1):
            for n2 in enumerate(nums2):
                if n1[1] == n2[1]:
                    print("auxList", auxList)
                    print("n1: ",n1 ," n2:", n2 ,"and last: " , last)
                    resultList.append([n1[0],n2[0]])
                    print("if", n2[0], "-",n1[0], "<", last[1], "-", last[0], "=", (n2[0]-n1[0] < last[1]-last[0]))
                    print("new: ", [n1[0],n2[0]] ,"\n")
                    if (n2[0]-n1[0] < last[1]-last[0]) and ():
                        if n1[0] > last[0] and n2[0] < last[1]:
                            auxList.pop()
                        # print("n1: ",n1," n2: ",n2, " n2[1] > last: ", n2[0] ,">", last)
                        auxList.append([n1[0],n2[0]])
                        last = [n1[0],n2[0]]
                        resultat += 1

        print("resultList", resultList)
        print("auxList", auxList)
        #  = [[resultList[0]]]
        # # slownik = {1 : resultList[0]}
        # i = 1
        # while i < len(resultList):
        #
        #
        #     print(resultList[i])
        #     print("i: ",i ," resultList[i][0]: ",resultList[i][0])
        #     print("auxList[len(auxList) - 1][i-1][0]: ", auxList[len(auxList) - 1][i-1][0])
        #     # print("auxList[len(auxList) - 1][1]: ", auxList[len(auxList) - 1][1])
        #     if  resultList[i][0] == auxList[len(auxList) - 1][len(auxList[i]) - 1][0]:# and resultList[i][1] < auxList[len(auxList) - 1][i-1][1]:
        #         auxList[len(auxList) - 1].append(resultList[i])
        #     elif resultList[i][0] > auxList[len(auxList) - 1][len(auxList[i]) - 1][0]:
        #         auxList.append(resultList[i])
        #     i += 1
        #     print(auxList)

        return resultat

    def maxUncrossedLinesInternet(self, a: list[int], b: list[int]) -> int:
        # @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if (max(
                dp(i - 1, j),
                dp(i, j - 1),
                dp(i - 1, j - 1) + int(a[i] == b[j]),
            )) > 1:
                print("dp(i - 1, j): ",dp(i - 1, j))
                print("dp(i, j - 1):",dp(i, j - 1))
                print("dp(i - 1, j - 1) + int(a[i] == b[j])",dp(i - 1, j - 1) + int(a[i] == b[j]))

            return max(
                dp(i - 1, j),
                dp(i, j - 1),
                dp(i - 1, j - 1) + int(a[i] == b[j]),
            )

        print("len(a) - 1:", len(a) - 1)
        print("len(b) - 1:", len(b) - 1)
        return dp(len(a) - 1, len(b) - 1)

Wynik = Solution()
nums1 = [1,3,7,1,7,5]
nums2 = [1,9,2,5,1]
# print(Wynik.maxUncrossedLines(nums1,nums2))

nums1 = [2,5,1,2,5]
nums2 = [10,5,2,1,5,2]
print(Wynik.maxUncrossedLinesInternet(nums1,nums2))