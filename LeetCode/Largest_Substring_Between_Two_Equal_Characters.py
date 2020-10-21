# Leetcode
# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_dist = -1
        starts = {}
        for i in range(len(s)):
            if s[i] in starts:
                max_dist = max(max_dist, i - starts[s[i]] - 1)
            else:
                starts[s[i]] = i
        return max_dist