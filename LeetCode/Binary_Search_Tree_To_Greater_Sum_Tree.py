# Leetcode
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0
        stack = []
        curr = root
        while curr or len(stack):
            if curr:
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
                total += curr.val
                curr.val = total

                curr = curr.left
        return root
