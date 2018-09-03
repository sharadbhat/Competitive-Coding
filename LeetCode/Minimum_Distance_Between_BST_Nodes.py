# LeetCode
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(root, l):
            if root.left:
                l = inorder(root.left, l)
            l.append(root.val)
            if root.right:
                l = inorder(root.right, l)
            return l

        minimum = None
        l = inorder(root, [])
        for i in range(len(l) - 1):
            if minimum == None or minimum > (l[i + 1] - l[i]):
                minimum = l[i + 1] - l[i]
        return minimum
