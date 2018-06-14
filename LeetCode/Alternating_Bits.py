# LeetCode
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = n & 1
        n = n >> 1
        while n > 0:
            if n & 1 == 1 and prev == 1:
                return False
            elif n & 1 == 0 and prev == 0:
                return False
            prev = n & 1
            n = n >> 1
        return True
