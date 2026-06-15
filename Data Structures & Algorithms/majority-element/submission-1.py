class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = len(nums)/2
        numsdict = {}
        for n in nums:
            numsdict[n] = 1 + numsdict.get(n, 0)
        return max(numsdict, key=numsdict.get)
        