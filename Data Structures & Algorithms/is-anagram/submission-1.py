from collections import defaultdict, Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s, dict_t = Counter(s), Counter(t)
        if dict_s != dict_t:
            return False
        return True