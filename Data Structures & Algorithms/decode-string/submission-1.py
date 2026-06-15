class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr = ""
                digit = ""
                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop() # pop [

                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit

                stack.append(int(digit) * substr) 
        return ''.join(stack)
