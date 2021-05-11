# Leetcode
# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        curr = root

        prev = None
        new_root = None

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if prev == None:
                    prev = curr
                    new_root = curr
                else:
                    prev.right = curr
                    prev.left = None
                    curr.left = None
                    prev = curr
                curr = curr.right

        return new_root
