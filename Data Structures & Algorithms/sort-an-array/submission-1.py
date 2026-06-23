class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # O(n^2) time complexity - bubble sort
        n = len(nums)
        for i in range(n):
            for j in range(n-1-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums