class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        i = 0
        j = len(height)-1
        leftMax = height[i]
        rightMax = height[j]
        water = 0   
        # [1,2,2,3]     
        while i < j:
            if leftMax < rightMax:
                i +=1
                leftMax = max(leftMax, height[i])
                water += leftMax - height[i]
            else:
                j-=1
                rightMax = max(rightMax, height[j])
                water += rightMax - height[j]
        return water