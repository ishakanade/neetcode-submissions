class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_map = {0:1}
        current_sum = 0
        for i in nums:
            current_sum += i
            result+= prefix_map.get(current_sum-k, 0)
            prefix_map[current_sum] = 1 + prefix_map.get(current_sum, 0)
        return result
        