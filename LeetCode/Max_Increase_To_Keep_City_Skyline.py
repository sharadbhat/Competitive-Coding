# Leetcode
# https://leetcode.com/problems/max-increase-to-keep-city-skyline/


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total = 0
        rowMax = []
        colMax = []
        for row in grid:
            rowMax.append(max(row))

        for col in range(len(grid)):
            colMax.append(max([row[col] for row in grid]))

        for row in range(len(grid)):
            for col in range(len(grid)):
                total += min(rowMax[row], colMax[col]) - grid[row][col]

        return total
