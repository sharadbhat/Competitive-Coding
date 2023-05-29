# Leetcode
# https://leetcode.com/problems/minimum-height-trees

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = set([i for i in range(n)])

        degrees = defaultdict(int)
        conn = defaultdict(set)

        for edge in edges:
            degrees[edge[0]] += 1
            degrees[edge[1]] += 1
            conn[edge[0]].add(edge[1])
            conn[edge[1]].add(edge[0])
        
        while True:
            if len(nodes) in [0, 1, 2]:
                break
            
            decrease = defaultdict(int)
            for node in degrees:
                if degrees[node] == 1:
                    nodes.remove(node)
                    degrees[node] = 0
                    parent = list(conn[node])[0]
                    decrease[parent] += 1
                    conn[parent].remove(node)
            
            for node in decrease:
                degrees[node] -= decrease[node]
        
        return list(nodes)
            