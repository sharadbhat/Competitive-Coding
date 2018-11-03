# LeetCode
# https://leetcode.com/problems/projection-area-of-3d-shapes/

class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        xy = sum([len([j for j in i if j != 0]) for i in grid])
        yz = sum([max(i) for i in grid])
        xz = sum([max([j[i] for j in grid]) for i in range(len(grid[0]))])
        return xy + yz + xz
