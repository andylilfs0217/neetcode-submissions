class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        q = [(0, [])]
        while q:
            new_q = []
            for total, combination_indexes in q:
                i = 0 if not combination_indexes else combination_indexes[-1]
                while i < n:
                    num = nums[i]
                    new_total, new_combination_indexes = total + num, combination_indexes + [i]
                    if new_total == target:
                        # get the result
                        new_combination = [nums[j] for j in new_combination_indexes]
                        ans.append(new_combination)
                    elif new_total < target:
                        new_q.append((new_total, new_combination_indexes))
                    i += 1
            q = new_q
        return ans