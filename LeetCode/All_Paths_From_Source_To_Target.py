# Leetcode
# https://leetcode.com/problems/all-paths-from-source-to-target/


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return self.getPaths(0, graph)

    def getPaths(self, curr: int, graph: List[List[int]]) -> List[List[int]]:
        if curr == len(graph) - 1:
            return [[curr]]

        out = []
        for node in graph[curr]:
            out += self.getPaths(node, graph)

        return [[curr] + i for i in out]
