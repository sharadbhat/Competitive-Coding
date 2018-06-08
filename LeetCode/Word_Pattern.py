# LeetCode
# https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern = [i for i in pattern]
        str = str.split()
        if len(pattern) != len(str):
            return False
        d = {}
        d_opp = {}
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != str[i]:
                    return False
            else:
                if str[i] not in d_opp:
                    d_opp[str[i]] = pattern[i]
                    d[pattern[i]] = str[i]
                else:
                    return False
        return True
