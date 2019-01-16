# LeetCode
# https://leetcode.com/problems/island-perimeter/

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def get_zeros(grid, x, y):
            return 4 - sum([grid[x][y - 1], grid[x - 1][y], grid[x + 1][y], grid[x][y + 1]])
        columns = len(grid[0])
        grid = [[0] * (columns + 2)] + [([0] + i + [0]) for i in grid] + [[0] * (columns + 2)]
        count = 0
        for row in range(1, len(grid) - 1):
            for column in range(1, len(grid[0]) - 1):
                count += get_zeros(grid, row, column) if grid[row][column] == 1 else 0
        return count
