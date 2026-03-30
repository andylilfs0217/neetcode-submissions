class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1
        while i < j:
            left, right = numbers[i], numbers[j]
            total = left + right
            if total == target:
                return [i+1, j+1]
            elif total > target:
                j -= 1
            else:
                i += 1

