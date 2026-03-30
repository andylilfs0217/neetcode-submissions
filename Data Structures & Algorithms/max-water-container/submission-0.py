class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n-1
        res = 0
        while i < j:
            hi, hj = heights[i], heights[j]
            inv = j - i
            water = min(hi, hj) * inv
            res = max(water, res)
            if hi < hj:
                i += 1
            else:
                j -= 1
        return res