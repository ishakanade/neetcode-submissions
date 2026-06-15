class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # #  sol3 (one pass algo)quick sort
        left, right = 0, len(nums)-1
        i = 0
        while i<=right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left +=1
            elif nums[i] == 2:
                nums[right],nums[i]= nums[i], nums[right]
                right -=1
                i -=1
            i +=1




        # sol 2 bubble sort ( high time complexity )
        # for i in range(len(nums)-1):
        #     for j in range(len(nums)-i-1):
        #         if nums[j]>nums[j+1]:
        #             temp = nums[j]
        #             nums[j] = nums[j+1]
        #             nums[j+1] = temp


        # solution 1 (did not work)
        # list1 = []
        # list2 = []
        # list3 = []
        # for i in nums:
        #     if i == 0:
        #         list1.append(i)
        #     elif i == 1:
        #         list2.append(i)
        #     else:
        #         list3.append(i)
        # nums = list1 + list2 + list3
        # cancelled list updation did not work
        