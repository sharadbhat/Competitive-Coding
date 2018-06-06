# LeetCode
# https://leetcode.com/problems/majority-element/description/

import math

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = int(math.floor(len(nums) // 2))
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
            if d[i] > length:
                return i
