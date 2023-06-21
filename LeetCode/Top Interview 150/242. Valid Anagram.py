# ╔═════════════════════════════════════════════════════════════════════════════════════════╗
# ║ Given two strings s and t, return true if t is an anagram of s, and false otherwise.    ║
# ║                                                                                         ║
# ║ An Anagram is a word or phrase formed by rearranging the letters of a different         ║
# ║ word or phrase, typically using all the original letters exactly once.                  ║
# ║                                                                                         ║
# ╚═════════════════════════════════════════════════════════════════════════════════════════╝

class Solution:
    def isAnagramInternet(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for ch in set(s):
            if s.count(ch) != t.count(ch):
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictS = dict()
        dictT = dict()

        for i in range(len(s)):
            if s[i] not in dictS:
                dictS[s[i]] = 1
            else:
                dictS[s[i]] += 1
            if t[i] not in dictT:
                dictT[t[i]] = 1
            else:
                dictT[t[i]] += 1

        return True if dictS == dictT else False


Wynik = Solution()

s = "anagram"
t = "nagaram"
Wynik1 = Wynik.isAnagram(s=s, t=t)
print("******\nWynik1", Wynik1, "\n******")

s = "rat"
t = "car"
Wynik1 = Wynik.isAnagram(s=s, t=t)
print("******\nWynik1", Wynik1, "\n******")
