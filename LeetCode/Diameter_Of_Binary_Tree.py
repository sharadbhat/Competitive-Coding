# Leetcode
# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_d = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def recurse(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            left = recurse(root.left) if root.left else 0
            right = recurse(root.right) if root.right else 0
            diameter = left + right
            self.max_d = max(diameter, self.max_d)
            return 1 + max(left, right)

        recurse(root)
        return self.max_d