class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        [30,38,30,36,35,40,28]
        [(40,5),(28,6)]
        [1,4,1,2,1,0,0]

        stack = list()
        n = len(temperatures)
        res = [0] * n
        for i, ni in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < ni:
                nj, j = stack.pop()
                res[j] = i-j
            stack.append((ni, i))
        return res