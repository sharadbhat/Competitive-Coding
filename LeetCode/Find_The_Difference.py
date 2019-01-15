# LeetCode
# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d1 = {}
        d2 = {}
        for i in s:
            d1[i] = d1.get(i, 0) + 1
        for i in t:
            d2[i] = d2.get(i, 0) + 1
        for i in d2:
            if i not in d1 or d1[i] != d2[i]:
                return i
