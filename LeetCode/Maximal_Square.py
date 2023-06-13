# Leetcode
# https://leetcode.com/problems/maximal-square

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        out = 0
        dp = []
        for _ in range(len(matrix)):
            dp.append([0 for _ in range(len(matrix[0]))])
        
        for row in range(len(matrix) - 1, -1, -1):
            for col in range(len(matrix[0]) - 1, -1, -1):
                if matrix[row][col] == '1':
                    if (row + 1) in range(len(matrix)) and (col + 1) in range(len(matrix[0])):
                        min_val = min(dp[row + 1][col], dp[row][col + 1])
                        if matrix[row + min_val][col + min_val] == '1':
                            dp[row][col] = 1 + min_val
                        else:
                            dp[row][col] = min_val
                    else:
                        dp[row][col] = 1
                    
                    out = max(out, dp[row][col])

        return out ** 2