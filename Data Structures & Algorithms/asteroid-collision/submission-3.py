class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and stack[-1]>0 and ast<0:
                diff = ast + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    ast = 0
                else:
                    stack.pop()
                    ast = 0
            if ast != 0:
                stack.append(ast)
        return stack 
        