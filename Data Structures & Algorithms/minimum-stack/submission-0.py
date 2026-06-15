class MinStack:

    def __init__(self):
        self.stack = []
        self.stackmin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stackmin.append(min(self.stackmin[-1], val) if self.stackmin else val)

    def pop(self) -> None:
        self.stack.pop()
        self.stackmin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackmin[-1]
        
