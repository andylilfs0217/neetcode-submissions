import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(a + b)
            elif token == '-':
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(a - b)
            elif token == '*':
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(a * b)
            elif token == '/':
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(int(a / b))
            else:
                stack.append(token)
            print(stack)
        ans = int(stack.pop())
        return ans