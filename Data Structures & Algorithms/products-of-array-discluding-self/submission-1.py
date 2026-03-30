class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        extended_n = n+2
        list_a, list_b = [1] * (extended_n), [1] * (extended_n)
        extended_nums = [1] + nums + [1]
        for i in range(1, extended_n):
            num_left, num_up_left = list_a[i-1], extended_nums[i-1]
            cell = num_left * num_up_left
            list_a[i] = cell
        for i in range(extended_n-2, 0, -1):
            num_right, num_up_right = list_b[i+1], extended_nums[i+1]
            cell = num_right * num_up_right
            list_b[i] = cell
        ans = []

        for i in range(1, extended_n-1):
            a, b = list_a[i], list_b[i]
            cell = a * b
            ans.append(cell)
        return ans


            