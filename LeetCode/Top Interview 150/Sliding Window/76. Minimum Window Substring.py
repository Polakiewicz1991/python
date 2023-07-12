from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        tCounter = dict(Counter(t))
        start, stop = 0, len(t)
        result = str()
        sCounterAux = dict(Counter(s[start:stop]))


        # for k in tKeys:

        # print(s[start:stop].count(k))
        # # while stop <= len(s):
        # print("1", sCounterAux)
        # print("1", s[start:stop])
        while start <= len(s) - 1:
            # sCounter = dict(Counter(s[start:stop]))
            # print(sCounter)
            try:
                contains = all(sCounterAux[item[0]] >= item[1] for item in tCounter.items())
            except KeyError:
                contains = False

            if contains == False and stop < len(s):

                if s[stop] not in sCounterAux:
                    sCounterAux[s[stop]] = 1
                else:
                    sCounterAux[s[stop]] += 1
                stop += 1
            else:
                if contains == True and (len(s[start:stop]) < len(result) or len(result) == 0):
                    result = s[start:stop]
                sCounterAux[s[start]] -= 1
                start += 1

            # print(start,stop)
            # print(sCounterAux)
            # print(start, stop, s[start:stop])

        # print(s[start-1:stop])
        return result

Wynik = Solution()

s, t = "ADOBECODEBANC", "ABC"
Wynik1 = Wynik.minWindow(s=s,t=t)
print("******\nWynik1", Wynik1, "\n******")

s, t = "a", "a"
Wynik1 = Wynik.minWindow(s=s,t=t)
print("******\nWynik1", Wynik1, "\n******")

s, t = "a", "aa"
Wynik1 = Wynik.minWindow(s=s,t=t)
print("******\nWynik1", Wynik1, "\n******")

s, t ="cabwefgewcwaefgcf", "cae"
Wynik1 = Wynik.minWindow(s=s,t=t)
print("******\nWynik1", Wynik1, "\n******")
