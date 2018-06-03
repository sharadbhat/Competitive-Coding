# LeetCode
# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if len(strs) > 0:
            for i in strs[0]:
                prefix += i
                present_in_all = True
                for j in strs:
                    if j.startswith(prefix) == False:
                        present_in_all = False
                        return prefix[:-1]
        return prefix
