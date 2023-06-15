# Given a square matrix mat, return the sum of the matrix diagonals.
#
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary
# diagonal that are not part of the primary diagona
class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:

        xLen = len(mat)

        for i in mat:
            yLen = len(i)
            if yLen != xLen:
                return 0

        x1 = 0
        x2 = yLen - 1
        y = 0
        sum = 0

        while y < xLen:
            sum += mat[y][x1]
            if x1 != x2:
                sum += mat[y][x2]
            # print("mat[y][x1]:", mat[y][x1])
            # print("mat[y][x2]:", mat[y][x2])
            #
            # print("x1: ", x1)
            # print("x2: ", x2)
            # print("y: ", y)

            print("\n")
            x1 += 1
            x2 -= 1
            y += 1

        return (sum)

    def diagonalSum2(self, mat: list[list[int]]) -> int:
        ans = 0
        # mat_len_even = len(mat)//2
        # mat_len_odd = len(mat)%2
        for i in range(len(mat) // 2):
            ans += sum([mat[i][i], mat[i][-1 - i], mat[-1 - i][i], mat[-1 - i][-1 - i]])
        if len(mat) % 2 != 0:
            ans += mat[len(mat) // 2][len(mat) // 2]
        return ans

    def diagonalSum3(self, mat: list[list[int]]) -> int:

        xLen = len(mat)

        for i in mat:
            yLen = len(i)
            if yLen != xLen:
                return 0

        x1 = 0
        x2 = xLen - 1
        sum = 0

        for y in mat:
            sum += y[x1]
            if x1 != x2:
                sum += y[x2]

            # print("y[x1]:", y[x1])
            # print("y[x2]",y[x2])

            x1 += 1
            x2 -= 1

        return (sum)


Wynik = Solution()
print("Wynik: ",Wynik.diagonalSum([ [1,2,3],
                                    [4,5,6],
                                    [7,8,9]]))
print("Wynik: ",Wynik.diagonalSum2([[1,2,3],
                                    [4,5,6],
                                    [7,8,9]]))
print("Wynik: ",Wynik.diagonalSum3([[1,2,3],
                                    [4,5,6],
                                    [7,8,9]]))