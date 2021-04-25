# Leetcode
# https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        leftCount = rightCount = 0
        if root.left:
            leftCount = self.countNodes(root.left)

        if root.right:
            rightCount = self.countNodes(root.right)

        return 1 + leftCount + rightCount
