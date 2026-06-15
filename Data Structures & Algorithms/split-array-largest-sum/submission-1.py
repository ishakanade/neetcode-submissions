class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = r
        while l <= r:
            m = l + (r-l)//2
            curr_sum = 0
            subarray_cnt = 1
            for i in range(len(nums)):
                curr_sum += nums[i]
                if curr_sum > m:
                    curr_sum = nums[i]
                    subarray_cnt += 1
            if subarray_cnt > k:
                l = m + 1
            elif subarray_cnt <= k:
                res = min(res, m)
                r = m - 1
        return res
