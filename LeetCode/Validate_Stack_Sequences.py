# LeetCode
# https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        j = 0
        for i in pushed:
            if i == popped[j]:
                j += 1
                while len(stack) > 0 and stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
            else:
                stack.append(i)
        while len(stack) > 0:
            if stack.pop() == popped[j]:
                j += 1
            else:
                break
        if j == len(popped):
            return True
        return False
