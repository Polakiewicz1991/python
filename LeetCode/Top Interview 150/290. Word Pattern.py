# ╔═════════════════════════════════════════════════════════════════════╗
# ║ Given a pattern and a string s, find if s follows the same pattern. ║
# ║                                                                     ║
# ║Here follow means a full match, such that there is a bijection       ║
# ║between a letter in pattern and a non-empty word in s.               ║
# ║                                                                     ║
# ╚═════════════════════════════════════════════════════════════════════╝

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
        sList = (s.split())
        sDict = dict()
        patternDict = dict()
        print(sList)

        if len(sList) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in sDict:
                sDict[pattern[i]] = {sList[i]}
            else:
                sDict[pattern[i]].add(sList[i])
                # print(len(lettersDictS[letter]))
                if len(sDict[pattern[i]]) > 1:
                    return False
            if sList[i] not in patternDict:
                patternDict[sList[i]] = {pattern[i]}
            else:
                patternDict[sList[i]].add(pattern[i])
                # print(len(lettersDictS[letter]))
                if len(patternDict[sList[i]]) > 1:
                    return False

        return True
Wynik = Solution()

pattern = "abba"
s = "dog cat cat dog"
Wynik1 = Wynik.wordPattern(s=s, pattern=pattern)
print("******\nWynik1", Wynik1, "\n******")

pattern = "abba"
s = "dog cat cat fish"
Wynik1 = Wynik.wordPattern(s=s, pattern=pattern)
print("******\nWynik1", Wynik1, "\n******")

pattern = "abba"
s = "dog dog dog dog"
Wynik1 = Wynik.wordPattern(s=s, pattern=pattern)
print("******\nWynik1", Wynik1, "\n******")

pattern ="aaa"
s ="aa aa aa aa"
Wynik1 = Wynik.wordPattern(s=s, pattern=pattern)
print("******\nWynik1", Wynik1, "\n******")