class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [4,10,23,25] h = 4
        high = max(piles)
        low = 1
        result = high
        # time = ceil(x / k)
        while low<=high:
            mid = (low + high) // 2
            time = 0
            for i in piles:
                time += math.ceil(i/mid)
            if time > h:
                low = mid + 1
            elif time <= h:
                high = mid - 1
                result = mid
        return result
