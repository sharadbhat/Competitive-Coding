# LeetCode
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            return self.preorder(root, [])
        return []

    def preorder(self, root, l):
        l.append(root.val)
        if root.left:
            l = self.preorder(root.left, l)
        if root.right:
            l = self.preorder(root.right, l)
        return l
