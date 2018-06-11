# LeetCode
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            return self.postorder(root, [])
        return []

    def postorder(self, root, l):
        if root.left:
            l = self.postorder(root.left, l)
        if root.right:
            l = self.postorder(root.right, l)
        l.append(root.val)
        return l
