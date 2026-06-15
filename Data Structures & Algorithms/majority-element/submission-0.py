class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = len(nums)/2
        numsdict = {}
        for i  in range(len(nums)):
            numsdict[nums[i]] = 1 + numsdict.get(nums[i], 0)
        return max(numsdict, key=numsdict.get)
        