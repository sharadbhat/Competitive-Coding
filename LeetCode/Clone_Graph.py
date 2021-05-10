# Leetcode
# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        return self.deepClone(node, dict())

    def deepClone(self, curr: 'Node', found_nodes: dict) -> 'Node':
        new_curr = Node(curr.val)
        found_nodes[new_curr.val] = new_curr

        for node in curr.neighbors:
            if node.val in found_nodes:
                new_curr.neighbors.append(found_nodes[node.val])
            else:
                new_curr.neighbors.append(self.deepClone(node, found_nodes))

        return new_curr
