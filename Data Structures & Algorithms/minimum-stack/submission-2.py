class MinStack:

    def __init__(self):
        self.Stack = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.Stack.append(val)
        if not self.MinStack or self.MinStack[-1] >= val:
            self.MinStack.append(val)

    def pop(self) -> None:
        val = self.Stack.pop()
        if val == self.MinStack[-1]:
           self.MinStack.pop()

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
