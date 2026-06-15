class Solution:
    # 10
    # 12
    # 11
    # 10
    # 1 1 1 5 4
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        subarray_len = len(nums)
        left = 0
        sum = 0
        window_len= 0
        assert_true = False
        for right in range(len(nums)):
            sum += nums[right]
            if sum >= target:
                assert_true = True
                while sum >= target:
                    subarray_len = min(subarray_len, right - left + 1)
                    sum -= nums[left]
                    left +=1
        if not assert_true:
            subarray_len = 0
        return subarray_len