# LeetCode
# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in d1:
                d1[s[i]] += 1
            else:
                d1[s[i]] = 1

            if t[i] in d2:
                d2[t[i]] += 1
            else:
                d2[t[i]] = 1

        if d1 == d2:
            return True
        return False
