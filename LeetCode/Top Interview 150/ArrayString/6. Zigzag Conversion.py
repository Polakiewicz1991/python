# Input: s = "PAYPALISHIRING", numRows = 4
# Output: " PINALSIGYAHRPI"
#           PINALSIGYAHRPI
#           PINALSIGYAHRPI
# sLen:  14  numRowInt:  3  numRowMod:  2
# Explanation:
# P[0]          I[6]            N[12]
# A[1]     L[5] S[7]      I[11] G[13]
# Y[2] A[4]     H[8] R[10]
# P[3]          I[9]
#Nr 0       1      2       3       4       5       6
#0  [0,0]                 6[3,0]                  12[6,0]
#1  [0,1]         5[2,1]  7[3,1]          11[5,1] 13[6,1]
#2  [0,2]  4[1,2]         8[3,2]  10[4,2]
#3  [0,3]                 9[3,3]

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#          PAHNAPLSIIGYIR
# P   A   H   N
# A P L S I I G
# Y   I   R
class Solution:
    def convert2(self, s: str, numRows: int) -> str:
        sLen = len(s)
        numRowInt = len(s) // numRows
        numRowMod = len(s) % numRows

        sResult: str = ""

        i = 0
        j = 0
        index = 0
        while i < sLen:
            j = 0
            print("i: ",i)
            index = ((numRowInt + numRowMod)  * j) + i
            while index < sLen:
                index = ((numRowInt + numRowMod)  * j) + i
                print("index: ", index)

                if index < sLen:
                    sResult += s[index]
                    print(sResult)
                j += 1
            i += 1


        print("sLen: ", sLen , " numRowInt: ", numRowInt , " numRowMod: ", numRowMod)

    def convert(self, strConvert: str, numRows: int) -> str:
        lista :list[list]= ['']*numRows

        i = 0
        j = 0
        k = 0
        while i < len(strConvert):
            # print("i: ", i)
            # print("j: ", j)
            # print("k: ", k)
            # print("\n")
            if j % (numRows - 1) == 0:
                lista[k] += strConvert[i]

                if k == (numRows-1):
                    j += 1
                    k -= 1
                else:
                    k += 1
            else:
                lista[k] += strConvert[i]
                k -= 1
                j += 1
            i += 1

        i = 0
        strResult= ""
        while i < numRows:
            strResult += lista[i]
            # print(strResult)
            i += 1
        return strResult

    def convert3(self, strConvert: str, numRows: int) -> str:
        lista :list[list]= ['']*numRows

        j = 0
        k = 0
        if numRows > 1:
            for i, s in enumerate(strConvert):
                # print("j: ", j)
                # print("k: ", k)
                # print("\n")
                if j % (numRows - 1) == 0:
                    lista[k] += s

                    if k == (numRows-1):
                        j += 1
                        k -= 1
                    else:
                        k += 1
                else:
                    lista[k] += s
                    k -= 1
                    j += 1

            i = 0
            strResult= ""
            for i in lista:
                strResult += i
                # print(strResult)
            return "".join(lista)
        else:
            return strConvert

    def convert4(self, st: str, numRows: int) -> str:
        if numRows == 1 or len(st) <= numRows:
            return st
        L = [''] * numRows
        print(L)
        i, s = 0 ,1
        for ss in st:
            L[i] += ss
            if i == 0:
                s = 1
            elif i >= numRows - 1:
                s = -1
            i += s
        print(L)
        return ''.join(L)

Wynik = Solution()
print(Wynik.convert("PAYPALISHIRING",3))
print(Wynik.convert4("PAYPALISHIRING",4))