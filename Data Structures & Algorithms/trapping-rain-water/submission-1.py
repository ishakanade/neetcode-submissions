class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        # vol_i = min(left_heighest_bar, right_highest_bar) - height[i]
        vol = 0
        l = leftmax = 0
        leftmax = height[l]
        r = len(height)-1
        rightmax = height[r]
        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax = max(leftmax, height[l])
                vol += leftmax - height[l]
            else:
                r-=1
                rightmax = max(rightmax, height[r])
                vol += rightmax - height[r]
        return vol
