class MinStack:

    def __init__(self):
        self.Stock = list()
    def push(self, val: int) -> None:
        self.Stock.append(val)
    def pop(self) -> None:
        self.Stock.pop()
    def top(self) -> int:
        print(self.Stock[len(self.Stock) - 1])
        print(self.Stock[- 1])
        return self.Stock[len(self.Stock) - 1]
    def getMin(self) -> int:
        print(min(self.Stock))
        return min(self.Stock)

    def __str__(self):
        return f"{self.Stock}"

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); #return -3
minStack.pop();
minStack.top();    #return 0
minStack.getMin(); # return -2
print(minStack)