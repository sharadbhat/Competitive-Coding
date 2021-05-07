# LeetCode
# https://leetcode.com/problems/first-unique-character-in-a-string/


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] = -1
            else:
                d[s[i]] = i

        first = None
        for i in d:
            if d[i] != -1:
                if first == None or d[i] < first:
                    first = d[i]
        return first if first != None else -1
