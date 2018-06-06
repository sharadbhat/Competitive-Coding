# LeetCode
# https://leetcode.com/problems/excel-sheet-column-number/description/

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            count += ((26 ** (len(s) - 1 - i)) * (ord(s[i]) - 64))

        return count
