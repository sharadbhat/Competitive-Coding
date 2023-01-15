# Leetcode
# https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist = []
        for _ in range(len(mat)):
            dist.append([sys.maxsize] * len(mat[0]))

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    dist[row][col] = 0
                else:
                    if row > 0:
                        dist[row][col] = min(dist[row][col], dist[row - 1][col] + 1)
                    if col > 0:
                        dist[row][col] = min(dist[row][col], dist[row][col - 1] + 1)

        for row in range(len(mat) - 1, -1, -1):
            for col in range(len(mat[0]) - 1, -1, -1):
                if row < len(mat) - 1:
                    dist[row][col] = min(dist[row][col], dist[row + 1][col] + 1)
                if col < len(mat[0]) - 1:
                    dist[row][col] = min(dist[row][col], dist[row][col + 1] + 1)

        return dist