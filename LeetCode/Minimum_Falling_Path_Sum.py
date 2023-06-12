# Leetcode
# https://leetcode.com/problems/minimum-falling-path-sum

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        prev_level = matrix[0]

        for level in range(1, len(matrix)):
            new_level = []
            for i in range(len(matrix)):
                cost = sys.maxsize
                for j in range(i - 1, i + 2):
                    if j in range(len(matrix)):
                        cost = min(cost, matrix[level][i] + prev_level[j])
                new_level.append(cost)
            prev_level = new_level

        return min(prev_level)