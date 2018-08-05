# LeetCode
# https://leetcode.com/problems/leaf-similar-trees/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.traverse(root1, []) == self.traverse(root2, [])

    def traverse(self, root, l):
        if root.right == None and root.left == None:
            l.append(root.val)
        else:
            if root.right != None:
                l = self.traverse(root.right, l)
            if root.left != None:
                l = self.traverse(root.left, l)
        return l
