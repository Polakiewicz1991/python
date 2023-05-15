def lengthOfLongestSubstring(s: str) -> int:
    lista = []
    ciagZnakow = ""
    i = 0
    j = 0

    while i < (len(s)):
        # print(i)
        if i == 0:
            ciagZnakow += s[i]
        elif ciagZnakow.count(s[i]) > 0:
            # str(ciagZnakow)
            # print("ciagZnakow: ", ciagZnakow)
            lista.append([ciagZnakow,len(ciagZnakow)])
            i -= (len(ciagZnakow))
            ciagZnakow = ""
        else:
            ciagZnakow += s[i]
        i += 1

    def strLenght(lista :list):
        for i in (lista):
            # print("i[0]: ",i[0])
            # print("i[1]: ", i[1])
            yield i[1]

    print("range: ",range(len(lista)))

    def strMaxIndex(lista: list):
        maksymalnieIndex = 0
        i = 0
        while i < len(lista):
            # print("i[0]: ",i[0])
            # print("i[1]: ", i[1])
            if lista[i][1] > maksymalnieIndex:
                maksymalnieIndex = i
            i += 1
        return maksymalnieIndex

    print("lista: ",lista)
    maksymalnie = max(strLenght(lista))
    maksymalnieIndex = strMaxIndex(lista)
    print(maksymalnieIndex)

    print("najdłuższy ciąg znaków bez powtórzenia znaku ma : ", maksymalnie , " liter")
    # /nowa2 = [i + 2 for i in lista if i < 4]
    print("najdłuższy ciąg znaków bez powtórzenia znaku to: ", lista[maksymalnieIndex][0])

lengthOfLongestSubstring("asdfaghjkaaskqwertxfgfhgjkjlk'poiuytreweazdxcvbnnk.,mn vcgjklo;iluyutyrtdgfchjkjlk.nm,bnvncyuioaaapoiuytrewqasdfghjkl,mnbvcxzaa")


def lengthOfLongestSubstringInternet(s: str) -> int:
    char_set = set()
    max_len, start = 0, 0
    for i, c in enumerate(s):
        # print("i: ", i )
        while c in char_set:
            # print(" c: ", c)
            # print("char_set: ", char_set)
            char_set.remove(s[start])
            start += 1
        char_set.add(c)
        max_len = max(max_len, i - start + 1)
    return max_len

h = lengthOfLongestSubstringInternet("asdfaghjkaaskqwertxfgfhgjkjlk'poiuytreweazdxcvbnnk.,mn vcgjklo;iluyutyrtdgfchjkjlk.nm,bnvncyuioaaapoiuytrewqasdfghjkl,mnbvcxzaa")
print(h)