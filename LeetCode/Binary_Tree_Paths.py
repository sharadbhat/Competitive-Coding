# Leetcode
# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return

        left = self.binaryTreePaths(root.left) or []
        right = self.binaryTreePaths(root.right) or []

        out = []
        for i in left + right:
            out.append(str(root.val) + '->' + i)

        return out if len(out) else [str(root.val)]
