# LeetCode
# https://leetcode.com/problems/add-digits/description/

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            n = 0
            while num > 0:
                n += num % 10
                num //= 10
            num = n
        return num
