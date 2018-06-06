# LeetCode
# https://leetcode.com/problems/first-unique-character-in-a-string/description/

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        ones = []
        one_pos = {}
        orig_pos = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
                ones.append(s[i])
                one_pos[s[i]] = len(ones) - 1
                orig_pos[s[i]] = i
            else:
                d[s[i]] += 1
                if s[i] in one_pos:
                    ones[one_pos[s[i]]] = "_"
                    del one_pos[s[i]]

        if len(ones) > 0:
            for i in ones:
                if i != "_":
                    return orig_pos[i]
        return -1
