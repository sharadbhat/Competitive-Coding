# Leetcode
# https://leetcode.com/problems/convert-bst-to-greater-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.convertTree(root)
        return root

    def convertTree(self, root: TreeNode, total=0) -> int:
        if root.right:
            total = self.convertTree(root.right, total)

        root.val += total
        total = root.val

        if root.left:
            total = self.convertTree(root.left, total)

        return total
