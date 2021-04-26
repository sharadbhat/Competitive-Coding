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
        for i in range(len(nums)):
            heappush(heap, nums[i])
            if i >= k:
                heappop(heap)
        return heappop(heap)
