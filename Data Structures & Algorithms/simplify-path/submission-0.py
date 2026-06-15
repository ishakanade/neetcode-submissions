class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # neetcode practice ... .. courses .
        paths = path.split("/")
        for char in paths:
            if char=='' or char=='.':
                continue
            if char == '..':
                if stack:
                    stack.pop()
                continue
            stack.append(char)
        return '/' + '/'.join(stack)
