from typing import List
class Solution:
    def findSubstringInternet(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        result = []
        word_dict = {}

        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1

        for i in range(len(s) - total_len + 1):
            window = {}
            j = 0
            while j < total_len:
                word = s[i + j:i + j + word_len]
                if word in word_dict:
                    window[word] = window.get(word, 0) + 1
                    if window[word] > word_dict[word]:
                        break
                else:
                    break
                j += word_len
            if j == total_len:
                result.append(i)

        return result

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        wordsLen = wordLen * len(words)
        resultList = []

        def nextString(j):
            wordsAux = []
            for i in range(len(words)):
                # print(i+j, (i+j)*wordLen)
                wordsAux.append(s[(i * wordLen) + j:(i * wordLen) + j + wordLen])
            return wordsAux


        i = 0
        while i <= len(s) - wordsLen:
            wordsAux = nextString(i)
            print(i, ":", wordsAux)

            if s[i:i + wordLen] in wordsAux:
                # wordsAux = s[i:i + wordsLen]
                for w in words:
                    if w in wordsAux:
                        wordsAux.remove(w)
                        if len(wordsAux) == 0:
                            resultList.append(i)
            #     i += wordLen
            # else:
            i += 1

        return resultList

Wynik = Solution()

# s = "barfoothefoobarman"
# words = ["foo","bar"]
# Wynik1 = Wynik.findSubstring(s= s, words= words)
# print("******\nWynik1", Wynik1, "\n******")
#
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
# Wynik1 = Wynik.findSubstring(s= s, words= words)
# print("******\nWynik1", Wynik1, "\n******")
#
# s = "barfoofoobarthefoobarman"
# words = ["bar","foo","the"]
# Wynik1 = Wynik.findSubstring(s= s, words= words)
# print("******\nWynik1", Wynik1, "\n******")

s ="wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
Wynik1 = Wynik.findSubstring(s= s, words= words)
print("******\nWynik1", Wynik1, "\n******")

s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]
Wynik1 = Wynik.findSubstring(s= s, words= words)
print("******\nWynik1", Wynik1, "\n******")
