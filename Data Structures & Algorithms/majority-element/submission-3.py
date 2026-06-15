class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, result = 0,0
        for i in nums:
            if count == 0:
                result = i
            count = count + (1 if i == result else -1) 
        return result

        # numsdict = {}
        # for n in nums:
        #     numsdict[n] = 1 + numsdict.get(n, 0)
        # return max(numsdict, key=numsdict.get)
        