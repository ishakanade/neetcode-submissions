class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # maxw = max(weights)
        loww = max(weights)
        maxw = sum(weights)
        result = maxw
        while loww <= maxw:
            lwc = (loww + maxw) // 2
            print("lwc : ", lwc)
            dayscount = 0
            j = 0
            while j < len(weights):
                curr = 0
                while j < len(weights) and curr + weights[j] <= lwc:
                    curr += weights[j]
                    j +=1
                print(curr)
                dayscount +=1
            if dayscount <= days:
                maxw = lwc - 1
                result = lwc
            else:
                loww = lwc + 1
        return result
