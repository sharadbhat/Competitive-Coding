# Leetcode
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.getMin(root, 10 ** 6)

    def getMin(self, root: TreeNode, minDepth: int, currDepth=0) -> int:
        if not root:
            return 0

        if root and not root.left and not root.right:
            return min(minDepth, currDepth + 1)

        leftMin = rightMin = 10 ** 6

        if root.left:
            leftMin = self.getMin(root.left, minDepth, currDepth + 1)

        if root.right:
            rightMin = self.getMin(root.right, minDepth, currDepth + 1)

        return min(leftMin, rightMin)
