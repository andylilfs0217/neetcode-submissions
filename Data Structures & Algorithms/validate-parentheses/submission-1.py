class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = [s[0]]
        i = 1
        while i < len(s):
            curr = s[i]
            if len(stack) == 0:
                stack.append(curr)
                i += 1
                continue
            print(curr, stack)
            prev = stack.pop()
            corr = dictionary.get(curr, '')
            if prev != corr:
                stack.append(prev)
                stack.append(curr)
            i += 1

        ans = len(stack) == 0

        return ans