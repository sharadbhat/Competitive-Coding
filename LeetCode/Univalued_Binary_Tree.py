# LeetCode
# https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_tree(node, value):
            if node.val != value:
                return False
            if node.left:
                temp = check_tree(node.left, value)
                if temp == False:
                    return False
            if node.right:
                temp = check_tree(node.right, value)
                if temp == False:
                    return False
        val = root.val
        if check_tree(root, val) == None:
            return True
        return False
