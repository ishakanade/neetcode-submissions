class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        quad = []
        def ksum(k, start, target):
            if k == 2:
                left = start
                right = len(nums)-1
                while left<right:
                    total = nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -=1
                    else:
                        result.append(quad + [nums[left], nums[right]])
                        left +=1
                        right -=1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                return
            for i in range(start, len(nums)-k+1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                quad.append(nums[i])
                ksum(k-1, i+1, target-nums[i])
                quad.pop()
        ksum(4,0,target)
        return result