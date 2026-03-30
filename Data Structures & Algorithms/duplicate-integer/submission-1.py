class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared_num_set = set()
        for num in nums:
            if num not in appeared_num_set:
                appeared_num_set.add(num)
            else:
                return True

        return False