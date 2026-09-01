class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0
        while l <= r:
            mid = (l+r)//2  # l + ((r-l)//2)
            sq = mid * mid
            if sq > x:
                r = mid - 1
            elif sq < x:
                l = mid + 1
                res = mid # Find the largest m such that m * m <= x
            elif sq == x:
                return mid
        return res