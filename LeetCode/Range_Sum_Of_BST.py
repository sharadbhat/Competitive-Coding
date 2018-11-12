# LeetCode
# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root:
            values = self.inorder(root, [])
        total = 0
        for i in values:
            if i >= L and i <= R:
                total += i
        return total

    def inorder(self, root, l):
        if root.left:
            l = self.inorder(root.left, l)
        l.append(root.val)
        if root.right:
            l = self.inorder(root.right, l)
        return l
