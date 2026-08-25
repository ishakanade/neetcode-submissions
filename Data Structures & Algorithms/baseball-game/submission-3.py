class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        stack = []
        for c in operations:
            if c == '+':
                stack.append(stack[-1] + stack[-2])
                total +=stack[-1]
            elif c == 'C':
                total -=stack[-1]
                stack.pop()
            elif c == 'D':
                stack.append(stack[-1]*2)
                total +=stack[-1]
            else:
                stack.append(int(c))
                total += int(c)
        return total