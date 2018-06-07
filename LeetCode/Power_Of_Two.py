# LeetCode
# https://leetcode.com/problems/power-of-two/description/

import math

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return n == 2 ** round(math.log(n, 2))
