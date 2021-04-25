# Leetcode
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        prev = None
        minDiff = 10 ** 6
        stack = []
        curr = root

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                if prev is not None:
                    minDiff = min(minDiff, curr.val - prev)
                prev = curr.val
                curr = curr.right

        return minDiff
