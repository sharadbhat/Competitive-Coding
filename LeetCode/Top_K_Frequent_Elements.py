# LeetCode
# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        l = sorted(d, key=d.get, reverse=True)
        return l[:k]
