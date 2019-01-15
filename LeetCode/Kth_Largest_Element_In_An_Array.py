# LeetCode
# https://leetcode.com/problems/kth-largest-element-in-an-array/

from heapq import heappush, heapify, heappop

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in nums[:k]:
            heappush(heap, i)
        for i in nums[k:]:
            heappush(heap, i)
            heappop(heap)
        return heappop(heap)
