
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0

        s[::-1]
        print(s)
        print(s[::-1])

        for i in reversed(s): #s[::-1]
            if i == " " and res == 0:
                continue
            elif i == " " and res > 0:
                return res
            else:
                res += 1
        return res

    def lengthOfLastWordInternet(self, s: str) -> int:
        print(s.strip())
        print(s.strip().split(" "))
        print(s.strip().split(" ")[-1])

        return len(s.strip().split(" ")[-1])





Wynik = Solution()

s = "Hello World"
Wynik1 = Wynik.lengthOfLastWord(s= s)
print("Wynik1", Wynik1)

s = "   fly me        to   the moon     "
Wynik1 = Wynik.lengthOfLastWord(s= s)
print("Wynik1", Wynik1)

s = "luffy is still joyboy"
Wynik1 = Wynik.lengthOfLastWord(s= s)
print("Wynik1", Wynik1)