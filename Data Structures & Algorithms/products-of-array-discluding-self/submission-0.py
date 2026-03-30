class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0 for _ in range(n)]
        product_without_zero = 1
        for num in nums:
            if (num != 0):
                product_without_zero *= num

        num_of_0 = 0
        zero_idx = -1
        for i, num in enumerate(nums):
            if num == 0:
                num_of_0 += 1
                zero_idx = i
        if num_of_0 >= 2:
            return result
        elif num_of_0 == 1:
            result[zero_idx] = product_without_zero
        else:
            for i, num in enumerate(nums):
                result[i] = int(product_without_zero/num)
        return result
