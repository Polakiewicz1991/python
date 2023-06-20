# ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ Given two strings s and t, determine if they are isomorphic.                                                ║
# ║                                                                                                             ║
# ║ Two strings s and t are isomorphic if the characters in s can be replaced to get t.                         ║
# ║                                                                                                             ║
# ║ All occurrences of a character must be replaced with another character while preserving the order           ║
# ║ of characters. No two characters may map to the same character, but a character may map to itself.          ║
# ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lettersDictS = dict()
        lettersDictT = dict()

        for i, letter in enumerate(s):
            if letter not in lettersDictS:
                lettersDictS[letter] = {t[i]}
            else:
                lettersDictS[letter].add(t[i])
                # print(len(lettersDictS[letter]))
                if len(lettersDictS[letter]) > 1:
                    return False

            if t[i] not in lettersDictT:
                lettersDictT[t[i]] = {letter}
            else:
                lettersDictT[t[i]].add(letter)
                # print(len(lettersDictT[t[i]]))
                if len(lettersDictT[t[i]]) > 1:
                    return False
        print(lettersDictS)
        return True

Wynik = Solution()

s = "egge"
t = "adda"
Wynik1 = Wynik.isIsomorphic(s=s, t=t)
print("******\nWynik1", Wynik1, "\n******")

s = "badc"
t = "baba"
Wynik1 = Wynik.isIsomorphic(s=s, t=t)
print("******\nWynik1", Wynik1, "\n******")