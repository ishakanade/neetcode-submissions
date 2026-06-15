class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(pos, speed) for pos, speed in zip(position, speed)]
        pos_speed.sort(reverse=True)
        stack = []

        for p,s in pos_speed:
            # append first, pop later
            # stack.append((target - p) / s)
            # if len(stack) > 1 and stack[-1] <= stack[-2]:
            #     stack.pop()
            time = ((target - p)/s)
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)
        
        