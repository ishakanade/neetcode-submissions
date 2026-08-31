class FreqStack:

    def __init__(self):
        self.group = {}
        self.freq = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        curr_cnt = self.freq.get(val, 0) + 1
        self.freq[val] = curr_cnt

        if curr_cnt > self.max_freq:
            self.group[curr_cnt] = []
            self.max_freq = curr_cnt

        self.group[curr_cnt].append(val)

    def pop(self) -> int:
        result = self.group[self.max_freq].pop()
        self.freq[result] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -=1

        return result


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()