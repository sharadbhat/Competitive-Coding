# LeetCode
# https://leetcode.com/problems/rotate-string/description/

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True

        for i in range(1, len(A)):
            if (A[-i:] + A[:-i]) == B:
                return True
        return False
