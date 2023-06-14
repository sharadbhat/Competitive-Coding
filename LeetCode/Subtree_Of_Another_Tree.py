# Leetcode
# https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        out = False
        if root.val == subRoot.val:
            out = self.sameTree(root, subRoot, subRoot)
        
        if out:
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sameTree(self, node1, node2, subRoot):
        if not node1 or not node2:
            return node1 == node2

        if node1.val == node2.val:
            if self.sameTree(node1.left, node2.left, subRoot) and self.sameTree(node1.right, node2.right, subRoot):
                return True
        
        return False