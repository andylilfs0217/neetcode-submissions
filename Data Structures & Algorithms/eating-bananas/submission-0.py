class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.minEatingSpeed1(piles, h)

    def minEatingSpeed1(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for pile in piles:
                hour = math.ceil(pile / mid)
                hours += hour
            if hours <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
