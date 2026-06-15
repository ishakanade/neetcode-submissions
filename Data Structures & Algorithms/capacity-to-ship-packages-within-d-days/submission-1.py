class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        loww = max(weights)
        maxw = sum(weights)
        result = maxw
        while loww <= maxw:
            lwc = (loww + maxw) // 2
            print("lwc : ", lwc)
            dayscount = 1
            curr = 0
            for j in weights:
                if curr + j <= lwc:
                    curr += j
                else: 
                    curr = j
                    dayscount +=1
            if dayscount <= days:
                result = lwc
                maxw = lwc - 1
            else:
                loww = lwc + 1
        return result
