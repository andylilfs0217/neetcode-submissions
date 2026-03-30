class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        lm = 100
        res = 0
        for price in prices:
            profit = price - lm
            res = max(res, profit)
            lm = min(price, lm)
        return res