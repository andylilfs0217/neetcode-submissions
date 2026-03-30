class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = dict()
        for i, num in enumerate(nums):
            if num in sum_dict:
                return list(sorted([i, sum_dict[num]]))
            diff = target - num
            sum_dict[diff] = i
        
