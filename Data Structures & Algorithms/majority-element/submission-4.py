class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        return sorted_nums[len(nums)//2]
        
        # threshold = len(nums)/2
        # hashmap = {}
        # for i in range(len(nums)):
        #     hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
        # return max(hashmap, key=hashmap.get)
