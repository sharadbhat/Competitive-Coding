# Leetcode
# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m - 2, -1, -1):
            grid[i][n - 1] += grid[i + 1][n - 1]
        for j in range(n - 2, -1, -1):
            grid[m - 1][j] += grid[m - 1][j + 1]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]