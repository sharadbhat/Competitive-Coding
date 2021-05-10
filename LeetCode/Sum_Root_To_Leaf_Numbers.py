# Leetcode
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return sum([int(i) for i in self.getPath(root)])

    def getPath(self, root: TreeNode) -> List[int]:
        if not root.left and not root.right:
            return [str(root.val)]

        val1, val2 = [], []
        if root.left:
            val1 = self.getPath(root.left)
        if root.right:
            val2 = self.getPath(root.right)

        out = []
        for i in val1 + val2:
            out.append(str(root.val) + i)

        return out
