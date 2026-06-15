class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_map = defaultdict(int)
        result = []
        for i in nums:
            nums_map[i] +=1
            if len(nums_map)<=2:
                continue
            
            nums_new = defaultdict(int)
            for num,count in nums_map.items():
                if count > 1:
                    nums_new[num] = count - 1
            nums_map = nums_new
        for num in nums_map:
            if nums.count(num) > len(nums)//3:
                result.append(num)
        return result