# ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ Given a string s representing a valid expression, implement a basic calculator to evaluate it,                  ║
# ║ and return the result of the evaluation.                                                                        ║
# ║                                                                                                                 ║
# ║ Note: You are not allowed to use any built-in function which evaluates strings                                  ║
# ║ as mathematical expressions, such as eval().                                                                    ║
# ║                                                                                                                 ║
# ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        lastSign = str()
        print(s)
        sum = 0
        def calcAux(s: str, sum: int) ->int:

            for i, n in enumerate(s):
                if n == '+' or n == '-':
                    lastSign = n
                elif n == '(':
                    calcAux(s=s[i:])
                elif n == ')':
                    return sum
                else:
                    pass



Wynik = Solution()

s = " 2-1 + 2 "
Wynik1 = Wynik.calculate(s=s)
print("******\nWynik1", Wynik1, "\n******")

s = "(1+(4+5+2)-3)+(6+8)"
Wynik1 = Wynik.calculate(s=s)
print("******\nWynik1", Wynik1, "\n******")

