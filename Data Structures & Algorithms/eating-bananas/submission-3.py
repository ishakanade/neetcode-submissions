class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = k = max(piles)

        # time = x // k
        while l <= r:
            mid = (l+r)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            if time <= h:
                r = mid - 1
                k = min(k, mid)
            elif time > h:
                l = mid + 1
        return k