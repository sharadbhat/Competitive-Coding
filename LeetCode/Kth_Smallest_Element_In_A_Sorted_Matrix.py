# LeetCode
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l = []
        for i in matrix:
            l += i
        return sorted(l)[k - 1]
