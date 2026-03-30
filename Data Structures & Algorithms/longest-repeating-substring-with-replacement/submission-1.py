class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        i, j = 0, k
        res = k
        counter = Counter(s[i:j+1])
        while j < n:
            max_occur = 0
            max_char = None
            for char, occur in counter.items():
                if occur > max_occur:
                    max_char = char
                    max_occur = occur
            length = j-i+1
            to_change = length - max_occur
            if to_change <= k:
                res = max(res, length)
                j += 1
                if j < n:
                    counter[s[j]] = counter.get(s[j], 0) + 1
            else:
                counter[s[i]] -= 1
                i += 1
        return res
