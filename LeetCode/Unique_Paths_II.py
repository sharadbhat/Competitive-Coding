# Leetcode
# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        for i in range(m):
            for j in range(n):
                obstacleGrid[i][j] = 0 if obstacleGrid[i][j] == 1 else 1

        for i in range(m - 2, -1, -1):
            obstacleGrid[i][n - 1] *= obstacleGrid[i + 1][n - 1]
        for j in range(n - 2, -1, -1):
            obstacleGrid[m - 1][j] *= obstacleGrid[m - 1][j + 1]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] != 0:
                    obstacleGrid[i][j] = obstacleGrid[i + 1][j] + obstacleGrid[i][j + 1]

        return obstacleGrid[0][0]