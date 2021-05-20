# Leetcode
# https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if not root:
            return ''

        if not root.left and not root.right:
            return str(root.val)

        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        if left:
            left = '(' + left + ')'
        if right:
            right = '(' + right + ')'
            if not left:
                left = '()'

        return str(root.val) + left + right
