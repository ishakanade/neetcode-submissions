class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = distance / speed
        # sort them in dec order of position
        # stack
        # if top time < curr time that means fleet 
        # need to append time which are greater and create fleet
        fleet_list = []
        stack = []
        for i in range(len(position)):
            distance = target - position[i]
            fleet_list.append([position[i], distance / speed[i]])
        
        fleet_list.sort(reverse=True)
        for pos, time in fleet_list:
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)

