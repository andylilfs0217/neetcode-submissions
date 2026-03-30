class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l_min, r_max = [], []
        temp = prices[0]
        for i, price in enumerate(prices):
            l_min.append(min(temp, price))
            temp = min(temp, price)
        temp = prices[-1]
        for i in range(n-1, -1, -1):
            r_max.append(max(temp, prices[i]))
            temp = max(temp, prices[i])
        r_max = r_max[::-1]

        ans = 0
        for i in range(n):
            ans = max(ans, r_max[i] - l_min[i])
        return ans


