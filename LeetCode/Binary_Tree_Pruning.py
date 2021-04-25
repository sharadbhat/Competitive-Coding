# Leetcode
# https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root.left:
            root.left = self.pruneTree(root.left)

        if root.right:
            root.right = self.pruneTree(root.right)

        if not root.left and not root.right:
            if root.val == 0:
                return None
            return root

        return root
