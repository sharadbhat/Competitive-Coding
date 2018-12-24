# LeetCode
# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        new_s = ""
        pos = [i for i in range(numRows)]
        positions = []
        i = 0
        while i < len(s):
            positions += pos[:]
            positions += pos[1:-1][::-1]
            i += (2 * numRows - 2)
        for i in range(numRows):
            for j in range(len(s)):
                if positions[j] == i:
                    new_s += s[j]
        return new_s
