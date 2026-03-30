class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        while len(nums_set) > 0:
            curr_res = 1
            curr = nums_set.pop()
            prv = curr - 1
            nxt = curr + 1
            while nxt in nums_set:
                curr_res += 1
                nums_set.discard(nxt)
                nxt += 1
            while prv in nums_set:
                curr_res += 1
                nums_set.discard(prv)
                prv -= 1
            res = max(curr_res, res)
        return res
