class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        max_length = 0
        current_length = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if abs(nums[i+1] - nums[i]) == 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length+1)
                current_length = 0
        return max(max_length, current_length+1)
        