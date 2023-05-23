def LongestCommonPrefix(strs :list[str]) -> str:
    minlenght = []
    listlenght = len(strs)
    StrResult  = ""

    for x in strs:
        minlenght.append(len(x))

    minlenght = min(minlenght)

    for i in range(0,minlenght):
        print(strs[1:])
        add = True
        j = 0
        if minlenght > 1:
            for j in range(0, listlenght - 1):
                if strs[j][i] == strs[j + 1][i]:
                    add = add
                else:
                    return StrResult
        if add == True:
            StrResult += strs[j][i]

    return StrResult
def longestCommonPrefixinernet(v: list[str]) -> str:
    ans = ""
    v = sorted(v)
    print("v:  ",v)
    first = v[0]
    print("first: ", first)
    last = v[-1]
    print("last: ", last)
    for i in range(min(len(first), len(last))):
        if (first[i] != last[i]):
            return ans
        ans += first[i]
    return ans

def longestCommonPrefixinernet2(strs: list[str]) -> str:
    if len(strs) == 0:
        return ""
    base = strs[0]
    for i in range(len(base)):
        for word in strs[1:]:
            print(word[i])
            if (i == len(word)) or word[i] != base[i]:
                return base[0:i]
    return base


print(LongestCommonPrefix(["abradowac","abraham","abrakadabra","abraksas","abram"]))
print(LongestCommonPrefix(["abradowac","abram","abrakadabra","abraham","abraksas"]))
print(LongestCommonPrefix(["abradowac","abram","abrakadabra","abraham","abraksas"]))
print(LongestCommonPrefix(["a"]))

