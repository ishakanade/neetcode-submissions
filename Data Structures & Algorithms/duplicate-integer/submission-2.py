class Solution:
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     nums2 = list(set(nums))
    #     if len(nums)!=len(nums2):
    #         return True
    #     return False

    def hasDuplicate(self, nums: List[int]) -> bool:
        numsset = set()
        for i in nums:
            if i in numsset:
                return True
            numsset.add(i)
        return False
        