class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        while l <= r:
            mid = (l+r)//2
            row = mid//m
            col = mid%m
            cell = matrix[row][col]
            if cell == target:
                return True
            elif cell > target:
                r = mid - 1
            else:
                l = mid + 1
        return False