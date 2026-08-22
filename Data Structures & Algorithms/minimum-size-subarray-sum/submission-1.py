class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_sum = 0
        min_subarr = float('inf')
        # or else min_subarr = len(nums) and assert_true=False
        for r in range(len(nums)):
            curr_sum +=nums[r]
            while curr_sum >= target:
                # assert_true = True
                min_subarr = min(min_subarr, r-l+1)
                curr_sum -= nums[l]
                l+=1
        if min_subarr == float('inf'):
            # if not assert_true
            return 0
        else:
            return min_subarr