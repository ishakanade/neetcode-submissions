class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[j+1] = nums[i]
                j +=1
        return j+1
        # i = 0
        # j = i + 1
        # while j<len(nums):
        #     if nums[i] == nums[j]:
        #         nums.pop(i)
        #     else:
        #         i +=1
        #         j +=1
        # return len(nums)