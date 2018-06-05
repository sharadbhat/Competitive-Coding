# LeetCode
# https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.split()) == 0:
            return 0
        else:
            return len(s.split()[-1])
