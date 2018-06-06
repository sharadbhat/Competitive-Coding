# LeetCode
# https://leetcode.com/problems/excel-sheet-column-number/description/

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s) - 1):
            count = (count + (ord(s[i]) - 64)) * 26

        count += (ord(s[-1]) - 64)
        return count
