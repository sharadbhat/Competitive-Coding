# Leetcode
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.getDepth(root)

    def getDepth(self, root: TreeNode, depth=0) -> int:
        if not root:
            return 0
        return max(depth + 1, self.getDepth(root.left, depth + 1), self.getDepth(root.right, depth + 1))
