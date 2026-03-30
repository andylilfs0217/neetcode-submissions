class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter = Counter(s)
        for char in t:
            if s_counter.get(char, 0) == 0:
                return False
            s_counter[char] -= 1
        for val in s_counter.values():
            if val > 0:
                return False
        return True
