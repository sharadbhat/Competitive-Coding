# Leetcode
# https://leetcode.com/problems/matrix-diagonal-sum/


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        mid = len(mat) // 2
        for i in range(mid):
            total += mat[i][i] + mat[i][~i] + mat[~i][i] + mat[~i][~i]

        if len(mat) % 2 != 0:
            return total + mat[mid][mid]

        return total
