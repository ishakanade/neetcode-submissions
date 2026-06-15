class Solution:
    def isValid(self, s: str) -> bool:
        parmap = {']':'[', '}':'{', ')': '('}
        stack = []
        for i in s:
            if i in parmap:
                if not stack or stack.pop()!= parmap[i]:
                    return False
            else:
                stack.append(i)

        return not stack            
