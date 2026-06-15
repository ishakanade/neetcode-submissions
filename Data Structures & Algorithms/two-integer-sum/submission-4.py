class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap and hashmap[diff] != i:
                return [i, hashmap[diff]]
        

        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if diff in hashmap:
        #         return [hashmap[diff],i]
        #     hashmap[num] = i