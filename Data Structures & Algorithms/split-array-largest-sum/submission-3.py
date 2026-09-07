class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        result = r
        # nums = [1,0,2,3,5], k = 4
        # sum = 11 max = 5 mid = 8
        # [1,0,2,3][5] mid = 8 k = 2 we want to minimize mid by splitting better
        # l = 5, r=7 m = 6
        # [1,0,2,3][5] mid = 6
        # [1,0,2][3][5] mid = 5 k<5
        # nums = [5,0,2,4,3], k = 4

        while l<=r:
            mid = (l+r)//2
            curr_total = 0
            temp_k = 1
            for num in nums:
                if curr_total + num > mid:
                    temp_k+=1
                    curr_total = num
                else:
                    curr_total += num
            if temp_k <= k:
                r = mid - 1
                result = mid
            else:
                l = mid + 1
        return result