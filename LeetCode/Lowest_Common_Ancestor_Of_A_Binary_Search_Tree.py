# LeetCode
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        output = root
        p, q = p.val, q.val
        while True:
            if output.val > p and output.val > q:
                output = output.left
            elif output.val < p and output.val < q:
                output = output.right
            else:
                return output
