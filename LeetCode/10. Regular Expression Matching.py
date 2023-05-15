import re
class Solution:
    def isMatch(self, inString: str, inPattern: str) -> bool:
        #s == "mississippi" and p =="mis*is*ip*.": TRUE
        if len(inPattern) >= len(inString):
            i = 0
            j = 0
            while i < len(inString) - 1:
                # print("len(inString) - 1:",len(inString) - 1)
                # print("i: ",i)
                # print("j: ",j)
                if j < len(inPattern):
                    # print("inPattern[j]:", inPattern[j])
                    # print("inString[i]:",inString[i])
                    # print("inPattern[j-1]:", inPattern[j-1])
                    if inPattern[j] == inString[i] or inPattern[j] == '.':
                        i += 1
                        j += 1
                    elif  (inPattern[j] == '*'):
                        if inPattern[j - 1] == inString[i] or inPattern[j - 1] == '.':
                            i += 1
                            j += 1
                        else:
                            j += 1
                            i = 0
                    else:
                        j += 1
                        # i = 0
                else:
                    return False
            return True

        else:
            return False

    class Solution:
        def isMatch(self, inString: str, inPattern: str) -> bool:
            resultBool = False
            resultBool = re.match(inPattern,inString)

            return True

Wynik = Solution()
print(Wynik.isMatch("aab","c*a*b"))
print(Wynik.isMatch("ab",".*c"))