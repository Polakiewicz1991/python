class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:

            sum = 0
            print("questions: ",questions, "\n")
            quest    = list(enumerate(questions))
            i,res = 0,0

            while i < len(quest):
                print("\n**********************")
                print("quest",quest)
                print("quest[i]", quest[i])
                print("quest[i][0]", quest[i][0])
                print("quest[i][1]", quest[i][1])
                points = quest[i][1][0]
                print("quest[i][1][0] - points", points)
                bp = quest[i][1][1]
                print("quest[i][1][1] - brainpower", bp)
                print("\n")
                sum = quest[i][1][0]

                k = 0
                j = quest[i][1][1] + quest[i][0] + 1
                print("next index: ",j)

                while j < len(questions):
                    print("sum pre: ", sum)
                    sum += quest[j][1][0]
                    print("sum after: ", sum)
                    print("j - next point: ", j,  " quest[j][1][0]: " , quest[j][1][0])
                    j += quest[j][1][1] + 1 + k
                i += 1
                res = max(res,sum)
                # print("res: ", res ," sum: ", sum)



            return res

    def mostPoints(self, questions: list[list[int]]) -> int:

            sum = 0
            print("questions: ",questions, "\n")
            quest    = list(enumerate(questions))
            i,res = 0,0

            while i < len(quest):
                print("\n**********************")
                print("quest",quest)
                print("quest[i]", quest[i])
                print("quest[i][0]", quest[i][0])
                print("quest[i][1]", quest[i][1])
                points = quest[i][1][0]
                print("quest[i][1][0] - points", points)
                bp = quest[i][1][1]
                print("quest[i][1][1] - brainpower", bp)
                print("\n")

                k = 0
                while k < len(quest):
                    sum = quest[i][1][0]
                    j = quest[i][1][1] + quest[i][0] + k + 1
                    print("next index: ",j," k: ", k)

                    while j < len(questions):
                        # print("sum pre: ", sum)
                        sum += quest[j][1][0]
                        # print("sum after: ", sum)
                        print("j - next point: ", j,  " quest[j][1][0]: " , quest[j][1][0])
                        j += 1 #quest[j][1][1] + 1
                    res = max(res,sum)
                    print("\nMax: ",res,"\n")
                    k += 1
                i += 1

                # print("res: ", res ," sum: ", sum)



            return res

#<editor-fold desc="test">
    # def mostPoints(self, questions: list[list[int]]) -> int:
    def mostPointsAux(self, questions: list[list[int]],index: int,nextIndex: int,sum: int, res: int) -> int:
        print("\nindex",index)
        print("nextIndex: ", nextIndex)
        print("sum: ",sum)
        print("res: ",res)

        if index == len(questions) - 1:
            print("*********\nDONE\n*********! ",res)
            return res

        if nextIndex > len(questions) - 1:
            print("2 - GO deeper")
            print(questions)
            index += 1
            nextIndex = index
            res = max(res, sum)
            self.mostPointsAux(questions, index,nextIndex, 0, res)

        if nextIndex + questions[nextIndex][1] + 1 < len(questions):
            sum += questions[nextIndex][0]
            print("1\tsum: ",sum)
            nextIndex += questions[nextIndex][1] + 1
            res = max(res, sum)
            self.mostPointsAux(questions,index,nextIndex,sum,res)

        elif nextIndex + questions[nextIndex][1] + 1 > len(questions):
            print("3\tsum + questions[nextIndex][0]: ",sum + questions[nextIndex][0])
            res = max(res, sum + questions[nextIndex][0])
            nextIndex += 1
            # if nextIndex > len(questions):
            return res
            # else:
            #     self.mostPointsAux(questions,index, nextIndex, sum, res)

        return res

# </editor-fold>
    def mostPoints(self, questions: list[list[int]]) -> int:
        memo = [-1] * len(questions)

        def dp(i):
            print("dp(i): ", i, " len(questions): ",len(questions))
            if i >= len(questions):
                return 0

            if memo[i] != -1:
                print("memo[i]: ",memo[i])
                return memo[i]

            # skip i th question and go to next
            skip = dp(i + 1)
            print("skip: ",skip)
            # solve i th question and go to next available question
            solve = questions[i][0] + dp(i + questions[i][1] + 1)
            print("solve: ",solve)

            memo[i] = max(skip, solve)
            return memo[i]

        return dp(0)




Wynik = Solution()
# questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
# Wynik1 = Wynik.mostPoints(questions)
questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# questions = [[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]
# Wynik2 = Wynik.mostPoints(questions)
# questions = [[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]
print(questions)
Wynik3 = Wynik.mostPointsAux(questions,0,0,0,0)
# questions = [[43,5]]
# questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# Wynik4 = Wynik.mostPoints(questions)
# questions = [[21,2],[1,2],[12,5],[7,2],[35,3],[32,2],[80,2],[91,5],[92,3],[27,3],[19,1],[37,3],[85,2],[33,4],[25,1],[91,4],[44,3],[93,3],[65,4],[82,3],[85,5],[81,3],[29,2],[25,1],[74,2],[58,1],[85,1],[84,2],[27,2],[47,5],[48,4],[3,2],[44,3],[60,5],[19,2],[9,4],[29,5],[15,3],[1,3],[60,2],[63,3],[79,3],[19,1],[7,1],[35,1],[55,4],[1,4],[41,1],[58,5]]
# Wynik5 = Wynik.mostPoints(questions)
# print("Wynik 1: ",Wynik1) #5
# print("Wynik 2: ",Wynik2) #7

print("Wynik 3: ",Wynik3) #157
# print("Wynik 4: ",Wynik4) #43
# print("Wynik 5: ",Wynik5) #781