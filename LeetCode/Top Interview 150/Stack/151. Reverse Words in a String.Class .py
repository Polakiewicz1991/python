class Solution:
    def reverseWords(self, s: str) -> str:
        #print(s.strip())
        # strList = s.strip().split(" ")[::-1]
        strList= s.strip().split()[::-1]
        print("strList: ",strList)
        strResult = ""
        for word in strList:
            if word != '':
                strResult += (word + " ")
        strResult.strip()
        print("result: ",strResult)

        return strResult

    def reverseWordsInternet(self, s: str) -> str:
        s1 = s.split()[::-1]
        # print(s1)
        l = []
        for i in s1:
            l.append(i)
            # print(l)
        s = " ".join(l)
        return s

Wynik = Solution()

s = "the sky is blue"
Wynik1 = Wynik.reverseWords(s= s)
print("Wynik1", Wynik1)

s = "  hello world  "
Wynik1 = Wynik.reverseWords(s= s)
print("Wynik1", Wynik1)

s = "a good   example"
Wynik1 = Wynik.reverseWords(s= s)
print("Wynik1", Wynik1)