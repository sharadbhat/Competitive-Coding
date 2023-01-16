# Leetcode
# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        orange_count = 0
        queue = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    orange_count += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))
        
        if orange_count == 0:
            return 0

        time = -1
        while len(queue) > 0:
            temp = queue[:]
            queue = []
            time += 1
            while len(temp) > 0:
                row, col = temp.pop(0)

                for x, y in zip([row, row, row - 1, row + 1], [col - 1, col + 1, col, col]):
                    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                        continue
                    if grid[x][y] == 1:
                        orange_count -= 1
                        grid[x][y] = 2
                        queue.append((x, y))

        return time if orange_count == 0 else -1