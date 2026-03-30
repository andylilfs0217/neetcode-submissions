class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        us = set()
        i, j = 0, 0
        res = 0
        while j < n:
            ci, cj = s[i], s[j]
            length = j-i+1
            if i == j:
                us.add(cj)
                res = max(res, length)
                j += 1
            elif cj not in us:
                us.add(cj)
                res = max(res, length)
                j += 1
            else:
                while i < j and cj in us:
                    us.discard(ci)
                    i += 1
                    ci = s[i]
                us.add(cj)
                j += 1
        res = max(res, j-i)
        return res
