class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] < pivot:
                    i +=1
                    arr[j], arr[i] = arr[i], arr[j]
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return i+1
        
        def quicksort(arr, low, high):
            if low < high:
                p = partition(arr, low, high)

                quicksort(arr, low, p-1)
                quicksort(arr, p+1, high)
            return arr
        
        quicksort(nums, 0, len(nums)-1)

        

        # n = len(nums)
        # for i in range(n):
        #     for j in range(n - 1 - i):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        # return nums