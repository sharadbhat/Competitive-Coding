# LeetCode
# https://leetcode.com/problems/transpose-matrix

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        l = []
        for i in range(len(A[0])):
            row = []
            for j in range(len(A)):
                row.append(A[j][i])
            l.append(row)
        return l
