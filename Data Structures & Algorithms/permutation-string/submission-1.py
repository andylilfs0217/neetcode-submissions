class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = [0] * 26
        counter = [0] * 26
        k, n = len(s1), len(s2)

        def get_counter_idx(c: str) -> int:
            return ord(c) - ord('a')

        for char in s1:
            s1_counter[get_counter_idx(char)] += 1

        for char in s2[:k]:
            counter[get_counter_idx(char)] += 1
        
        for i in range(n-k+1):
            if s1_counter == counter:
                return True
            j = i+k

            counter[get_counter_idx(s2[i])] -= 1
            if j < n:
                counter[get_counter_idx(s2[j])] += 1
        
        return False