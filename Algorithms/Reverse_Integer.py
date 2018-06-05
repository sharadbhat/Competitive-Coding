# LeetCode
# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            negative = True
            x = int(str(abs(x))[::-1])
        else:
            x = int(str(x)[::-1])
        
        if x > 2**31 - 1:
            x = 0
        if negative == True:
            return -x
        return x
