class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y, x = len(matrix), len(matrix[0])
        n = x * y
        l, r = 0, n-1

        ans = False

        while not ans and l <= r:
            m = (l + r) // 2
            i, j = m // x, m % x
            curr = matrix[i][j]
            if curr == target:
                ans = True
            elif curr > target:
                r = m - 1
            else:
                l = m + 1
            pass

        return ans