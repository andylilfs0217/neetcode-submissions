class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pmap = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        for char in s:
            if len(stack) > 0 and stack[-1] == pmap.get(char, ''):
                stack.pop()
            else:
                stack.append(char)
        res = len(stack) == 0
        return res