# ╔═════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ Given an array of strings strs, group the anagrams together.                                    ║
# ║ You can return the answer in any order.                                                         ║
# ║                                                                                                 ║
# ║ An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, ║
# ║ typically using all the original letters exactly once.                                          ║
# ║                                                                                                 ║
# ╚═════════════════════════════════════════════════════════════════════════════════════════════════╝

from typing import List

class Solution:
    def groupAnagramsOld(self, strs: List[str]) -> List[List[str]]:
        wordsList = list()
        def checkIfAnageam(s,t):
            try:
                if len(s) != len(t):
                    return False
            except TypeError:
                return False
            for ch in set(s):
                if s.count(ch) != t.count(ch):
                    return False
            return True

        wordsList = [[strs[0]]]
        strsLen = len(strs)
        for j in range(1,strsLen):
            word = strs[j]
            isAnagram = False
            for i, wL in enumerate(wordsList):
                if checkIfAnageam(wL[0],word):
                    isAnagram = True
                    # if word not in wL[0]:
                    wordsList[i].append(word)
            if isAnagram == False:
                print(wL,word)
                wordsList.append([word])
            j += 1
        # print("wordsList", wordsList)
        return wordsList

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for word in strs:
            sorted_word="".join(sorted(word))
            if sorted_word not in dic:
                dic[sorted_word]=[word]
            else:
                dic[sorted_word].append(word)
        return dic.values()

Wynik = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Wynik1 = Wynik.groupAnagrams(strs=strs)
print("******\nWynik1", Wynik1, "\n******")

strs =["",""]
Wynik1 = Wynik.groupAnagrams(strs=strs)
print("******\nWynik1", Wynik1, "\n******")

