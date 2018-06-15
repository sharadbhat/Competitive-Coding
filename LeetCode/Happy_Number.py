# LeetCode
# https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = set()
        while True:
            temp = 0
            while n > 0:
                x = n % 10
                temp += x ** 2
                n //= 10
            if temp == 1:
                return True
            if temp in a:
                return False
            a.add(temp)
            n = temp
