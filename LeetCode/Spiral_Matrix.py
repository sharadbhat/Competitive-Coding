# Leetcode
# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        curr_dir = 0
        row, col = 0, 0

        visited_count = 0
        visited = []
        for _ in range(len(matrix)):
            visited.append([False] * len(matrix[0]))
        
        out = []
        while visited_count < len(matrix) * len(matrix[0]):
            out.append(matrix[row][col])
            visited[row][col] = True
            visited_count += 1

            if curr_dir == 0:
                if (col + 1) >= len(matrix[0]) or visited[row][col + 1]:
                    curr_dir = 1
            elif curr_dir == 1:
                if (row + 1) >= len(matrix) or visited[row + 1][col]:
                    curr_dir = 2
            elif curr_dir == 2:
                if (col - 1) < 0 or visited[row][col - 1]:
                    curr_dir = 3
            else:
                if (row - 1) < 0 or visited[row - 1][col]:
                    curr_dir = 0

            if curr_dir == 0:
                col += 1
            elif curr_dir == 1:
                row += 1
            elif curr_dir == 2:
                col -= 1
            else:
                row -= 1

        return out