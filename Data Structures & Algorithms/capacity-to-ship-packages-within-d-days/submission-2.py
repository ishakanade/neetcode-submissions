class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r = sum(weights)
        l = max(weights)
        result = r

        while l <= r:
            mid = (l + r)//2
            d = 1
            total = 0
            for w in weights:
                if total + w > mid:
                    d +=1
                    total = 0
                total += w
            if d > days:
                l = mid + 1
            elif d <= days:
                r = mid -1
                result = min(result, mid)
        return result