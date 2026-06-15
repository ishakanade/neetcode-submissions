class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        contains1 = False
        for i in range(n):
            if nums[i] == 1:
                contains1 = True
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1
        if contains1 == False:
            return 1
        for i in nums:
            actual_index = abs(i) - 1
            if nums[actual_index] < 0:
                continue
            nums[actual_index] *= -1
        
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1