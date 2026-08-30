class Solution:
    def decodeString(self, s: str) -> str:
        # lets say s = "2[a3[b]]c" now i will append to stack till i get a ] once i get on ], i will pop and assign it to str then again pop to remove [ then again pop to get the int now s1 = int * str and i will again push this to stack will go on repeating until i reach end of input string once this is done i will return stack[-1]
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                temp_s = ''
                num = ''
                while stack and stack[-1] != '[':
                    temp_s = stack.pop() + temp_s
                stack.pop() #this will pop [
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * temp_s)
        return ''.join(stack)
