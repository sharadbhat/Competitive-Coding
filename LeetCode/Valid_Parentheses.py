# LeetCode
# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = []
        for i in s:
            if i in ['[', '{', '(']:
                a.append(i)
            elif i in [']', '}', ')']:
                if len(a) == 0:
                    return False
                if i == ']':
                    if a[-1] == '[':
                        del a[-1]
                    else:
                        return False
                elif i == '}':
                    if a[-1] == '{':
                        del a[-1]
                    else:
                        return False
                elif i == ')':
                    if a[-1] == '(':
                        del a[-1]
                    else:
                        return False
        if len(a) == 0:
            return True
        return False
