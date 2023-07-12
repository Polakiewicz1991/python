class Solution:
    def findSmallestSetOfVerticesBad(self, n: int, edges: list[list[int]]) -> list[int]:
        resList = []
        reachList = []
        for x in edges:
            print("x:",x)
            if x[0] not in resList and x[0] not in reachList:
                print("1")
                resList.append(x[0])
                reachList.append(x[1])

            elif x[0] in resList and x[1] not in reachList and x[0] not in  reachList:
                print("2")
                reachList.append(x[1])

            elif x[0] in reachList and x[1] not in reachList:
                print("3")
                reachList.append(x[1])

            if x[0] in resList and x[1] in resList:
                print("4!!!!!!!!!!!!!")
                resList.remove(x[1])

            # if x[0] in resList and x[1] not in reachList:
            #     reachList.append([x[1]])
            print("resList:",resList)
            print("reachList:", reachList)
            print("\n")

        return resList

    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        indegree = [0] * n
        starts = [0] * n
        for edge in edges:
            indegree[edge[1]] += 1
            starts[edge[0]] += 1
        print("indegree:", indegree)
        print("starts:", starts)
        #if there is no connection to elemenet, it must starts form it
        ans = []
        for i in range(n):
            if indegree[i] == 0 and starts[i] != 0:
                ans.append(i)

        return ans

Wynik = Solution()
n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Wynik1 = Wynik.findSmallestSetOfVertices(n= n,edges= edges) #[0,3]
print(Wynik1,"\n")
n = 5
edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Wynik2 = Wynik.findSmallestSetOfVertices(n= n,edges= edges) #[0,2,3]
print(Wynik2,"\n")
n = 4
edges =[[1,2],[3,2],[1,3],[1,0],[0,2],[0,3]]
Wynik3 = Wynik.findSmallestSetOfVertices(n= n,edges= edges) #[0,2,3]
print(Wynik3,"\n")