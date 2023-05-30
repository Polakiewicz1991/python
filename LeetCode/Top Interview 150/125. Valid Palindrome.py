class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        #usunięcie znaków specjalnych ze stringa
        s = "".join(ch for ch in s if ch.isalnum())
        s = s.lower()

        print(s)
        y = s[::-1]
        print(y)
        while i < len(s):
            if s[i] == y[i]:
                i += 1
            else:
                return False
        return True

Wynik = Solution()
s = "A man, a plan, a canal: Panama"
Wynik1 = Wynik.isPalindrome(s=s)
print("Wynik1", Wynik1)