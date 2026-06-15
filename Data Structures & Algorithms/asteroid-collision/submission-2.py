class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            alive = True
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if abs(stack[-1]) > abs(asteroids[i]):
                    alive = False
                    break
                elif abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    alive = False
                    break
                else:
                    stack.pop()
            if alive:
                stack.append(asteroids[i])
                # equal -> pop
                # top motha -> do not push
                # top lahan asel tr pop and push
                # stack.push(i)
        return stack
