from collections import defaultdict, Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        ans = False

        l, r = 0, m-1
        m_counter, n_counter = Counter(s1), Counter(s2[l:r+1])
        if m_counter == n_counter:
            ans = True

        match_dict = defaultdict(lambda: True)
        for char, m_freq in m_counter.items():
            n_freq = n_counter[char]
            if m_freq != n_freq:
                match_dict[char]= False

        while r < n-1 and not ans:
            n_counter[s2[l]] -= 1
            match_dict[s2[l]] = m_counter[s2[l]] == n_counter[s2[l]]
            l += 1
            r += 1
            n_counter[s2[r]] = n_counter.get(s2[r], 0) + 1
            match_dict[s2[r]] = m_counter[s2[r]] == n_counter[s2[r]]
            curr = True
            for v in match_dict.values():
                curr &= v
            ans = curr


        return ans