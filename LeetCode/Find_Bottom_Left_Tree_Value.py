# Leetcode
# https://leetcode.com/problems/find-bottom-left-tree-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        left = root.val
        queue = [root]
        while len(queue):
            for i in range(len(queue)):
                curr = queue.pop(0)
                if i == 0:
                    left = curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return left
