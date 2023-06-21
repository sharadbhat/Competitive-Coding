# Leetcode
# https://leetcode.com/problems/maximum-width-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        root.val = 1
        q = [root]

        widest = 0
        while len(q):
            left = q[0]
            right = q[-1]
            widest = max(widest, right.val - left.val + 1)

            length = len(q)
            for i in range(length):
                curr = q.pop(0)
                if curr.left:
                    curr.left.val = curr.val * 2
                    q.append(curr.left)
                if curr.right:
                    curr.right.val = curr.val * 2 + 1
                    q.append(curr.right)

        return widest
