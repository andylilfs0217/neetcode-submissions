class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '-', '*', '/'])
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                cal = 0
                match token:
                    case '+':
                        cal = num1 + num2
                    case '-':
                        cal = num1 - num2
                    case '*':
                        cal = num1 * num2
                    case '/':
                        cal = int(num1 / num2)
                stack.append(cal)
        res = stack.pop()
        return res
                