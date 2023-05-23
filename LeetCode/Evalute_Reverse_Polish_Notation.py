# Leetcode
# https://leetcode.com/problems/evaluate-reverse-polish-notation

# Good solution
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in '+-*/':
                b, a = stack.pop(), stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(int(a / b))
            else:
                stack.append(int(i))
        return stack[0]

# Works but slow
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(['+', '-', '/', '*'])
        tokens = [int(i) if i not in ops else i for i in tokens]
        while len(tokens) > 1:
            op1, op2 = None, None
            i = 0
            while tokens[i] not in ops:
                op1 = op2
                op2 = tokens[i]
                i += 1
            res = 0
            if tokens[i] == '+':
                res = op1 + op2
            elif tokens[i] == '-':
                res = op1 - op2
            elif tokens[i] == '*':
                res = op1 * op2
            else:
                res = int(float(op1)/op2)
            del tokens[i]
            del tokens[i - 1]
            tokens[i - 2] = res
        
        return tokens[0]