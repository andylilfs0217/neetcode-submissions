

"""
   2
 2   1
1 4 3 2


"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)

        l, r = 1, k
        while l <= r:
            m = (l+r)//2
            h_needed = 0
            for pile in piles:
                h_needed += int(math.ceil(pile / m))
            print(m, h_needed)
            if h_needed <= h:
                # Hours needed is fewer than the target Hour
                # But it fits the requirements
                # It's too fast
                # Find a smaller speed
                k = m
                r = m-1
            else:
                # Hours needed is larger than the target hour
                # Not enough hours
                # Find a faster speed
                l = m+1

        return k