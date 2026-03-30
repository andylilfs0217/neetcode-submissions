class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lm, rm, res = [0 for _ in range(n)], [0 for _ in range(n)], 0
        for i in range(1, n):
            lm[i] = max(height[i-1], lm[i-1])
        for i in range(n-2, -1, -1):
            rm[i] = max(height[i+1], rm[i+1])
        for i in range(n):
            res += max(min(lm[i], rm[i]) - height[i], 0)
        return res