class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1
        while i < j:
            left, right = numbers[i], numbers[j]
            diff = target - left
            if diff == right:
                return [i+1, j+1]
            if diff < right:
                j -= 1
            else:
                i += 1
            