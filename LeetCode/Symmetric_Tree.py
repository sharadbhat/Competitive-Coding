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
        return self.traverse(root.left) == self.traverse(root.right, reverse=True)

    def traverse(self, root: TreeNode, reverse=False) -> List[int]:
        if not root:
            return [None]
        else:
            if reverse:
                return [root.val] + self.traverse(root.right, True) + self.traverse(root.left, True)
            return [root.val] + self.traverse(root.left) + self.traverse(root.right)
