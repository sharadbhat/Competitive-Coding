# LeetCode
# https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        max_num = 0
        for i in nums:
            if i not in d:
                if max_num < i:
                    max_num = i
                d[i] = 1
        for i in range(0, max_num):
            if i not in d:
                return i
        return (max_num + 1)
