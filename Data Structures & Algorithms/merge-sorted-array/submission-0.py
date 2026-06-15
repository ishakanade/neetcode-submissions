class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1
        while j>=0:
            if i < 0:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
                continue
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -=1
                k -=1
            else:
                nums1[k] = nums1[i]
                # nums1[i] = nums2[j]
                k -= 1
                i-=1
        # if m == 0:
        #     for i in range(n):
        #         nums1[i] = nums2[i]
        # elif m > 0 and n >0:
        #     j = 0
        #     for i in range(m, m+n):
        #         nums1[i] = nums2[j]
        #         j +=1
        #     nums1 = sorted(nums1)
        
        