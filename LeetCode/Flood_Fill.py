# Leetcode
# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        queue = [(sr, sc)]
        while len(queue) > 0:
            row, col = queue.pop(0)
            if image[row][col] != color:
                image[row][col] = color
                for i, j in zip([row, row, row - 1, row + 1], [col - 1, col + 1, col, col]):
                    if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]):
                        continue
                    if image[i][j] == start_color:
                        queue.append((i, j))
        return image