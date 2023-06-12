# Leetcode
# https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        out = []
        reachable = {
            'pac': set(),
            'atl': set()
        }
        visited = {
            'pac': set(),
            'atl': set()
        }

        def dfs(x, y, ocean):
            reachable[ocean].add((x, y))
            
            for i, j in zip([x - 1, x, x, x + 1], [y, y - 1, y + 1, y]):
                if i in range(0, len(heights)) and j in range(0, len(heights[0])):
                    if (i, j) not in visited[ocean]:
                        if heights[i][j] >= heights[x][y]:
                            visited[ocean].add((i, j))
                            dfs(i, j, ocean)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    if (i, j) not in visited['pac']:
                        dfs(i, j, 'pac')
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    if (i, j) not in visited['atl']:
                        dfs(i, j, 'atl')

        intersection = reachable['pac'].intersection(reachable['atl'])
        return [list(i) for i in sorted(intersection)]
