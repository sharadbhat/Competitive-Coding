# LeetCode
# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in nums:
            if i in d:
                return True
            else:
                d[i] = 1
        return False
