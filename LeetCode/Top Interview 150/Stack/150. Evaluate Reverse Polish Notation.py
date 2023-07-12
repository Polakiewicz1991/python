# ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║ You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation. ║
# ║                                                                                                                 ║
# ║ Evaluate the expression. Return an integer that represents the value of the expression.                         ║
# ║                                                                                                                 ║
# ║ Note that:                                                                                                      ║
# ║                                                                                                                 ║
# ║     The valid operators are '+', '-', '*', and '/'.                                                             ║
# ║    Each operand may be an integer or another expression.                                                        ║
# ║    The division between two integers always truncates toward zero.                                              ║
# ║    There will not be any division by zero.                                                                      ║
# ║     The input represents a valid arithmetic expression in a reverse polish notation.                            ║
# ║     The answer and all the intermediate calculations can be represented in a 32-bit integer.                    ║
# ║                                                                                                                 ║
# ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stock = list()

        for n in tokens:
            if n.isnumeric() or (len(n) > 1 and n[0] == '-' and n[1:].isnumeric()):
                stock.append(int(n))
            else:
                if n == '+':
                    stock[-2] = stock[-1] + stock[-2]
                    stock.pop()
                elif n == '-':
                    stock[-2] = stock[-2] - stock[-1]
                    stock.pop()
                elif n == '*':
                    stock[-2] = stock[-1] * stock[-2]
                    stock.pop()
                elif n == '/':
                    stock[-2] = int(stock[-2] / stock[-1])
                    stock.pop()
            print(n.isnumeric() or (len(n) > 1 and n[0] == '-' and n[1:].isnumeric()), n, stock)

        return stock[0]
        # print(tokens[-1])
        # print(tokens[-2])
        # print(tokens[-3])
Wynik = Solution()

tokens = ["2","1","+","3","*"]
Wynik1 = Wynik.evalRPN(tokens=tokens)
print("******\nWynik1", Wynik1, "\n******")


tokens = ["4","13","5","/","+"]
Wynik1 = Wynik.evalRPN(tokens=tokens)
print("******\nWynik1", Wynik1, "\n******")

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Wynik1 = Wynik.evalRPN(tokens=tokens)
print("******\nWynik1", Wynik1, "\n******")
