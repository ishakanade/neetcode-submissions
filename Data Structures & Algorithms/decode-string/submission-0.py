class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr = []
                digit = []
                while stack and stack[-1] != '[':
                    substr.append(stack.pop())
                stack.pop() # pop [
                while stack and stack[-1].isdigit():
                    digit.append(stack.pop())
                substr = ''.join(reversed(substr))
                digit = ''.join(reversed(digit))

                word_to_append = int(digit) * substr
                stack.append(word_to_append) 
        return ''.join(stack)
