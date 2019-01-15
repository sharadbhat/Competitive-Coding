# LeetCode
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def get_inorder(root, l):
            if root.left:
                get_inorder(root.left, l)
            l.append(root.val)
            if root.right:
                get_inorder(root.right, l)
        l = []
        get_inorder(root, l)
        return l[k - 1]
