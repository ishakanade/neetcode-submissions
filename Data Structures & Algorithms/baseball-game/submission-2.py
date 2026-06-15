class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for i in operations:
            if i == "D":
                sum += (stack[-1] * 2)
                stack.append(stack[-1]*2)
            elif i == "C":
                sum -= stack[-1]
                stack.pop()
            elif i == "+":
                sum += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
                sum += stack[-1]

        return sum