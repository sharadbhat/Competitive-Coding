# LeetCode
# https://leetcode.com/problems/longest-common-prefix/description/


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''

        if len(strs) > 0:
            for i in range(len(strs[0])):
                char = strs[0][i]
                for j in strs[1:]:
                    if len(j) <= i or j[i] != char:
                        return prefix
                prefix += strs[0][i]

        return prefix
