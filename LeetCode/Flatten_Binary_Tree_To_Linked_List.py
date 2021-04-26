# Leetcode
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        prev = root
        curr = root
        while curr or len(stack):
            if curr:
                if curr != root:
                    prev.right = curr
                    prev = curr
                stack.append(curr.right)
                curr = curr.left
                prev.left = None
            else:
                curr = stack.pop()
