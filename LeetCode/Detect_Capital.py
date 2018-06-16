# LeetCode
# https://leetcode.com/problems/detect-capital/description/

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper():
            return True
        if word.islower():
            return True
        if word.istitle():
            return True
        return False
