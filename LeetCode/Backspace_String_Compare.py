# LeetCode
# https://leetcode.com/problems/backspace-string-compare/description/

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S1 = ""
        T1 = ""
        for i in S:
            if i == '#':
                S1 = S1[:-1]
            else:
                S1 += i

        for i in T:
            if i == '#':
                T1 = T1[:-1]
            else:
                T1 += i

        return S1 == T1
