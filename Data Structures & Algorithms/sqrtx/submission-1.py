class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l<=r:
            root = l + ((r-l)//2)
            square = root * root
            if square < x:
                l = root + 1
            elif square > x:
                r = root - 1
            else:
                return root
        # return l-1
        return r