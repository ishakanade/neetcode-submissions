class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # [5, 6] [1,2,3] -> 3
        A = nums1
        B = nums2
        if A>B:
            A,B = B,A
        total = len(A) + len(B)
        half = (total)//2
        # applying binary search
        l , r = 0, len(A)-1
        while True:
            A_mid = (l+r)//2
            B_mid = half - A_mid - 2
            # minusing 2 as 2 indices shift is required one for A and one for B
            
            Aleft = A[A_mid] if A_mid>=0 else float("-infinity")
            Bleft = B[B_mid] if B_mid>=0 else float("-infinity")
            Aright = A[A_mid+1] if (A_mid+1)<len(A) else float("infinity")
            Bright = B[B_mid+1] if (B_mid+1)<len(B) else float("infinity")

            if (Aleft <= Bright and Bleft <= Aright):
                if(total % 2 == 0):
                    return(max(Aleft, Bleft) + min(Aright, Bright))/2
                return min(Aright, Bright)
            elif (Aleft > Bright):
                r = A_mid - 1
            else:
                l = A_mid + 1




        
        
