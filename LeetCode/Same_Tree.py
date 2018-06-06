# LeetCode
# https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if self.traversal(p, []) == self.traversal(q, []):
            return True
        return False

    def traversal(self, a, l):
        leaf = False
        if a.left == None and a.right == None:
            leaf = True

        if a == None:
            return l

        if a.left != None:
            self.traversal(a.left, l)
        elif leaf == False:
            l.append(None)

        l.append(a.val)

        if a.right != None:
            self.traversal(a.right, l)
        elif leaf == False:
            l.append(None)
        
        return l
