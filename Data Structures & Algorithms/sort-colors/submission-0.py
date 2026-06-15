class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sol 2 bubble sort ( high time complexity )
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp


        # solution 1
        list1 = []
        list2 = []
        list3 = []
        for i in nums:
            if i == 0:
                list1.append(i)
            elif i == 1:
                list2.append(i)
            else:
                list3.append(i)
        nums = list1 + list2 + list3
        # cancelled list updation did not work
        