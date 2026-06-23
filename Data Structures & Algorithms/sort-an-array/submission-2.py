class Solution:
    def merge(self, left, right):
        i = 0
        j = 0
        result = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sortArray(self, nums: List[int]) -> List[int]:
        # O(nlogn) - merge sort
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)
        

        # O(n^2) time complexity - bubble sort
        # The -1 is needed because we compare: arr[j] and arr[j + 1] and j + 1 must stay within the array bounds.
        # n = len(nums)
        # for i in range(n):
        #     for j in range(n-1-i):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        # return nums