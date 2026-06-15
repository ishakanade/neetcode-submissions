class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = abs(i-j)
                if nums[i] == nums[j] and diff <=k:
                    return True
        return False