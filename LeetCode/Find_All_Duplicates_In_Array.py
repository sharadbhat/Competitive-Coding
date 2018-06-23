# LeetCode
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        repeated = []
        d = set()
        for i in nums:
            if i in d:
                repeated.append(i)
            else:
                d.add(i)
        return repeated
