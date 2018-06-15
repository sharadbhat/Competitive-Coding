# LeetCode
# https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        done = set()
        for i in range(len(s)):
            if s[i] in d and d[s[i]] != t[i]:
                return False
            elif s[i] not in d:
                if t[i] not in done:
                    d[s[i]] = t[i]
                    done.add(t[i])
                else:
                    return False
        return True
