# LeetCode
# https://leetcode.com/problems/nim-game/

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        return True
