class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for i in nums:
            if i in hashmap:
                return True
            hashmap.add(i)
        return False

        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False