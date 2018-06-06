# LeetCode
#https://leetcode.com/problems/implement-strstr/description/

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1
