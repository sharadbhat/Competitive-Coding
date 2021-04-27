# Leetcode
# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.checkSymmetry(root.left, root.right)

    def checkSymmetry(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return root1 == root2

        if root1 and root2:
            if root1.val != root2.val:
                return False

            return self.checkSymmetry(root1.left, root2.right) and self.checkSymmetry(root1.right, root2.left)
