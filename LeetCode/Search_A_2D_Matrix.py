# LeetCode
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row = 0
        for i in range(len(matrix)):
            if matrix[i][0] <= target:
                row = i
            else:
                break
        return target in matrix[row]
