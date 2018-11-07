# LeetCode
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        d = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}
        prev = s[0]
        count = d[prev]
        for i in s[1:]:
            if d[prev] <= d[i]:
                count += d[i]
            else:
                count -= d[i]
            prev = i
        return count
