# LeetCode
# https://leetcode.com/problems/groups-of-special-equivalent-strings/

class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return len({''.join(sorted(i[::2])) + ''.join(sorted(i[1::2])) for i in A})
