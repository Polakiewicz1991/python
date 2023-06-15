from typing import List
import numpy as np
from collections import Counter
class Solution:
    def equalPairsInternet(self, grid: List[List[int]]) -> int:
        pairs = 0
        cnt = Counter(tuple(row) for row in grid)
        print(cnt)
        for tpl in (grid):
            print(tpl)

        for tpl in zip(grid):
            print(tpl)

        for tpl in zip(*grid):
            print(tpl)
            pairs += cnt[tpl]
        return pairs

    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        matrix = np.array(grid)
        transposed_matrix = np.transpose(matrix)
        # print(matrix)
        # print(transposed_matrix)

        for x in range(len(grid)):
            for y in range (len(grid)):
                # print(x, matrix[x], y, transposed_matrix[y])
                if all(matrix[x] == transposed_matrix[y]):
                    # print(all(matrix[x] == transposed_matrix[y]), matrix[x])
                    res += 1

        return res


Wynik = Solution()

grid = [[3,2,1],[1,7,6],[2,7,7]]
Wynik1 = Wynik.equalPairs(grid= grid)
print("******\nWynik1", Wynik1, "\n******")

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Wynik1 = Wynik.equalPairs(grid= grid)
print("******\nWynik1", Wynik1, "\n******")

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Wynik1 = Wynik.equalPairsInternet(grid= grid)
print("******\nWynik1", Wynik1, "\n******")