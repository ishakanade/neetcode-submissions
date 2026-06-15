class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            # already sorted array
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            # binary search
            m = l + (r-l)//2
            res = min(res, nums[m])
            # [l , m,  r]
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return res

        # brute force
        # mini = float('inf')
        # for i in nums:
        #     mini = min(i, mini)
        # return mini
        # return min(nums)