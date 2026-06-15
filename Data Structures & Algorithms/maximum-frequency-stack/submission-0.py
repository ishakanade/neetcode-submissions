class FreqStack:

    def __init__(self):
        self.stack = {}
        self.count = {}
        self.maxval = 0        

    def push(self, val: int) -> None:
        valcnt = 1 + self.count.get(val,0)
        self.count[val] = valcnt
        if valcnt > self.maxval:
            self.maxval = valcnt
            self.stack[valcnt] = []
        self.stack[valcnt].append(val)
        

    def pop(self) -> int:
        result = self.stack[self.maxval].pop()
        self.count[result] = self.count.get(result,0) - 1
        if not self.stack[self.maxval]:
            self.maxval -=1
        return result


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()