class Solution:
    def validPalindrome(self, s: str) -> bool:
        list1 = list(s)
        list2 = list1[::-1]
        listLen = len(list1)
        oneDiff = False
        i = 0
        # while True:
        #     if list1[0:listLen-1] == list2[0:listLen-1]:
        #         return True
        #     list3 = [list2[-1]] + (list2[0:listLen-1])
        #     list2 = list3
        #     i += 1
        #     if (i == listLen):
        #         return False
        i = 0
        listAux = list1.copy()
        while True:
            list2 = listAux[::-1]
            print("listAux:",listAux,"list2:",list2," i:",i)

            if listAux[i] == list2[i]:
                continue
            else:
                listAux.pop(0)

    def validPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        while p1 <= p2:
            print("p1:",p1,"p2",p2,"s[p1] != s[p2]:",s[p1] != s[p2])
            if s[p1] != s[p2]:
                string1 = s[:p1] + s[p1 + 1:]
                string2 = s[:p2] + s[p2 + 1:]

                print("s[:p1]:",s[:p1],"s[p1 + 1:]:",s[p1 + 1:],"string1:",string1)
                print("s[:p2]:", s[:p2], "s[p2 + 1:]:", s[p2 + 1:], "string2:", string2)
                return string1 == string1[::-1] or string2 == string2[::-1]
            p1 += 1
            p2 -= 1
        return True

Wynik = Solution()

s = "1234561"
s2= "ccbbc"
Wynik1 = Wynik.validPalindrome(s)


print("Wynik1: ",Wynik1)