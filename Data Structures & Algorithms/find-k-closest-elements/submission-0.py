class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        r = len(arr) - k
        l = 0
        while l<r:
            mid = (r+l)//2
            if (x - arr[mid]) > (arr[mid+k] - x):
                l = mid + 1
            else:
                r = mid

        return arr[l:l+k]



        