from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_to_index_dict = defaultdict(int)
        for index, num in enumerate(nums):
            if num in diff_to_index_dict:
                diff_index = diff_to_index_dict[num]
                return [diff_index, index]
            diff = target - num
            diff_to_index_dict[diff] = index

