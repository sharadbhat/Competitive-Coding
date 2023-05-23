# Leetcode
# https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        
        def mark_visited(x, y):
            queue = [(x, y)]
            visited.add((x, y))
            while len(queue) > 0:
                tempx, tempy = queue.pop(0)
                directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
                for direction in directions:
                    r, c = tempx + direction[0], tempy + direction[1]
                    if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == '1' and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1' and (x, y) not in visited:
                    mark_visited(x, y)
                    count += 1

        return count