# Leetcode
# https://leetcode.com/problems/baseball-game/


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        total = 0

        for i in ops:
            if i == 'C':
                total -= stack.pop()
                continue
            elif i == 'D':
                stack.append(stack[-1] * 2)
            elif i == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
            total += stack[-1]
        return total
