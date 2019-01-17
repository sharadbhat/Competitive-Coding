# LeetCode
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root, l):
            if root.left:
                inorder(root.left, l)
            l.append(root.val)
            if root.right:
                inorder(root.right, l)
        l = []
        if root:
            inorder(root, l)
        return l
