# Leetcode
# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        diff = abs(left_depth - right_depth)

        return diff <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))
