from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)

        l, r = 0, 0

        char_set = set()
        curr_ans = 0
        while r < n:
            print(s[l:r+1])
            if s[r] not in char_set:
                char_set.add(s[r])
                r += 1
                curr_ans += 1
                ans = max(ans, curr_ans)
            else:
                while l < r and s[r] in char_set:
                    char_set.remove(s[l])
                    curr_ans -= 1
                    l += 1
                # char_set.add(s[r])

        return ans