# LeetCode
# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        d = {}
        new = []
        pos = {0: 0, 1: 0, 2: 0}
        for i in nums:
            d[i] = d.get(i, 0) + 1
            for j in [k for k in [1, 2] if k > i]:
                pos[j] += 1
            new.insert(pos[i], i)
        nums[:] = new[:]
