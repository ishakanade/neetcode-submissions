class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l = 0 
        r = mountainArr.length()-1
        # bsearch1 on entire array
        while l<=r:
            mid = (l+r)//2
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                l = mid + 1
            elif mountainArr.get(mid) > mountainArr.get(mid+1):
                r = mid - 1
            else:
                break
        # bsearch2 on left side as if target is found it would have lower index than that of right side target
        peak = mid
        l1 = 0
        r1 = peak
        while l1<=r1:
            mid = (l1+r1)//2
            if mountainArr.get(mid) > target:
                r1 = mid - 1
            elif mountainArr.get(mid) < target:
                l1 = mid + 1
            else:
                return mid
        # bsearch3
        # target not found in left side, searching on right side
        l2 = peak + 1
        r2 = mountainArr.length()-1
        while l2<=r2:
            mid = (l2+r2)//2
            if mountainArr.get(mid) > target:
                l2 = mid + 1
            elif mountainArr.get(mid) < target:
                r2 = mid - 1
            else:
                return mid
        # target not found in the array, returning -1
        return -1
