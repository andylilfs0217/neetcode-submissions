class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n

        stack = []
        for i, temp in enumerate(temperatures):
            while len(stack) > 0:
                last_temp, last_i = stack[-1]
                if temp > last_temp:
                    stack.pop()
                    ans[last_i] = i - last_i
                else:
                    break
                pass
            stack.append((temp, i))

        return ans