class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # [1,2|,3]
        # [2,4|,5,6]
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total//2
        if len(A) > len(B):
            A,B = B,A
        l, r = 0, len(A)-1
        while True:
            m = (l+r)//2
            n = half - m - 2 # m -1 and n - 1

            aleft = A[m] if m>=0 else float("-infinity")
            aright = A[m+1] if m+1<len(A) else float("infinity")
            bleft = B[n] if n>=0 else float("-infinity")
            bright = B[n+1] if n+1<len(B) else float("infinity")

            if aleft <= bright and bleft <= aright:
                if total % 2 == 0:
                    return(max(aleft,bleft) + min(aright,bright))/2
                return min(aright,bright)
            elif aleft > bright:
                r = m - 1
            else:
                l = m + 1
