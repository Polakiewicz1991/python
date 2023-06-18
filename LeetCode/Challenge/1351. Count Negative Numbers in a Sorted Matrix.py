
class Solution(object):
    def countNegatives(self, grid):
        res = 0
        for x in grid:
            # print(x, x.count(lambda y: y < 0 for y in x))
            # x.count()
            y = list(filter(lambda i:  i<0,x))
            res += len(y)#x.count(lambda x: x < 0)

        return res

Wynik = Solution()

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Wynik1 = Wynik.countNegatives(grid= grid)
print("******\nWynik1", Wynik1, "\n******")