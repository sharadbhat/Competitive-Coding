# LeetCode
# https://leetcode.com/problems/reverse-only-letters/description/

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letters = [i for i in S if i.isalpha()]
        letters = letters[::-1]

        out = ""
        count = 0
        for i in S:
            if i.isalpha():
                out += letters[count]
                count += 1
            else:
                out += i
        return out
