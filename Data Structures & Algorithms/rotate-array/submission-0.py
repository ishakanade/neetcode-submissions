class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def reverse(start, end):
            l, r = start, end
            while l<r:
                nums[l], nums[r]= nums[r], nums[l]
                l +=1
                r -=1
        # [1, 2,3,4,5] and k =2
        # first reversal will result in reversal of whole string
        # [5,4,3,2,1]
        reverse(0,len(nums)-1)
        # second reversal will rotate last k elements to first
        # [4,5,3,2,1]
        reverse(0, k-1)
        # third reversal will push start elements by k positions
        # [4,5,1,2,3]
        reverse(k, len(nums)-1)