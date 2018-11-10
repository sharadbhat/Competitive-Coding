# LeetCode
# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for i in strs:
            sorted_word = ''.join(sorted(i))
            d[sorted_word] = d.get(sorted_word, []) + [i]
        return [d[i] for i in d]
