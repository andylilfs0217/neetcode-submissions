from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        num_counter = defaultdict(int)
        while len(nums_set) > 0:
            start = nums_set.pop()
            num_counter[start] += 1
            curr = start + 1
            ans = max(ans, num_counter[start])
            flag = True
            while flag:
                if curr in nums_set:
                    num_counter[start] += 1
                    nums_set.remove(curr)
                    curr += 1
                elif curr in num_counter:
                    num_counter[start] += num_counter[curr]
                    del num_counter[curr]
                    flag = False
                else:
                    flag = False
                ans = max(ans, num_counter[start])
        return ans