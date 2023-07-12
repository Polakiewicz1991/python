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
        pass


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
