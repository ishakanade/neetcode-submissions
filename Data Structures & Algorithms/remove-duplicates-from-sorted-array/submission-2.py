class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
        # i = 0
        # j = i + 1
        # while j<len(nums):
        #     if nums[i] == nums[j]:
        #         nums.pop(i)
        #     else:
        #         i +=1
        #         j +=1
        # return len(nums)