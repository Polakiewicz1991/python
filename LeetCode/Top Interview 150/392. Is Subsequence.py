class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        startIndex = 0
        for x in s:
            if x in t[startIndex:]:
                print("startIndex: ", startIndex, " ", t[startIndex:])
                startIndex += t[startIndex:].index(x) + 1
            else:
                return False
        return True



Wynik = Solution()

s = "abc"
t = "ahbgdc"
Wynik1 = Wynik.isSubsequence(s= s, t= t)
print("Wynik1", Wynik1)

s = "axc"
t = "ahbgdc"
Wynik1 = Wynik.isSubsequence(s= s, t= t)
print("Wynik1", Wynik1)

s = "aaaaaa"
t = "bbaaaa"
Wynik1 = Wynik.isSubsequence(s= s, t= t)
print("Wynik1", Wynik1)