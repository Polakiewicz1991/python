class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

Wynik = Solution()

haystack = "sadbutsad"
needle = "sad"
Wynik1 = Wynik.strStr(haystack= haystack, needle= needle)
print("Wynik1",Wynik1)

haystack = "leetcode"
needle = "leeto"
Wynik1 = Wynik.strStr(haystack= haystack, needle= needle)
print("Wynik1",Wynik1)