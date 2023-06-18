# ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ Given two strings ransomNote and magazine, return true if ransomNote can be constructed                 ║
# ║ by using the letters from magazine and false otherwise.                                                 ║
# ║                                                                                                         ║
# ║ Each letter in magazine can only be used once in ransomNote.                                            ║
# ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════╝

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dictRansomNote = dict()
        dictMagazine = dict()

        i = 0
        iLen = max(len(ransomNote),len(magazine))
        while i < iLen:
            if i < len(ransomNote):
                if ransomNote[i] in dictRansomNote:
                    dictRansomNote[ransomNote[i]] += 1
                else:
                    dictRansomNote[ransomNote[i]] = 1
            if i < len(magazine):
                if magazine[i] in dictMagazine:
                    dictMagazine[magazine[i]] += 1
                else:
                    dictMagazine[magazine[i]] = 1

            i += 1

        for key in dictRansomNote.keys():
            if key not in dictMagazine.keys():
                return False
            if dictRansomNote[key] > dictMagazine[key]:
                return False

        return True

Wynik = Solution()

ransomNote = "a"
magazine = "b"
Wynik1 = Wynik.canConstruct(ransomNote= ransomNote, magazine=magazine)
print("******\nWynik1", Wynik1, "\n******")

ransomNote, magazine = "aa", "aab"
Wynik1 = Wynik.canConstruct(ransomNote= ransomNote, magazine=magazine)
print("******\nWynik1", Wynik1, "\n******")