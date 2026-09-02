class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l1, r1 = 0, rows-1

        while l1<=r1:
            mid1 = (l1 + r1)//2
            if matrix[mid1][-1] < target:
                l1 = mid1+1
            elif matrix[mid1][0] > target:
                r1 = mid1-1
            else:
                break
        l2, r2 = 0, cols-1

        while l2<=r2:
            mid2 = (l2 +r2)//2
            if matrix[mid1][mid2] < target:
                l2 = mid2+1
            elif matrix[mid1][mid2] > target:
                r2 = mid2-1
            else:
                return True
        return False

