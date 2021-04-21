# LeetCode
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        values = []
        queue = [(root, 0)]
        while len(queue) > 0:
            curr, depth = queue.pop(0)
            level = values.pop(depth) if len(values) > depth else []
            level.append(curr.val)
            values.insert(depth, level)
            if curr.left:
                queue.append((curr.left, depth + 1))
            if curr.right:
                queue.append((curr.right, depth + 1))
        return values
