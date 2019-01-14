# LeetCode
# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.sums = {}
        for row in range(len(matrix)):
            self.sums[row] = {}
            for col1 in range(len(matrix[0])):
                self.sums[row][col1] = {}
                for col2 in range(col1 + 1, len(matrix[0]) + 1):
                    self.sums[row][col1][col2 - 1] = sum(matrix[row][col1:col2])

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        value = 0
        for row in range(row1, row2 + 1):
            value += self.sums[row][col1][col2]
        return value


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
