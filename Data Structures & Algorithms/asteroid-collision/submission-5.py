class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            alive = True
            # collision will only happen when top is moving to left and new one to right
            while stack and stack[-1]>0 and i<0:
                if abs(stack[-1]) > abs(i):
                    alive = False
                    break
                elif abs(stack[-1]) < abs(i):
                    stack.pop()
                else:
                    stack.pop()
                    alive = False
                    break
            if alive:
                stack.append(i)
                # equal -> pop
                # top motha -> do not push
                # top lahan asel tr pop and push
                # stack.push(i)
        return stack